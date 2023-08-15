import torch
from transformers import BertTokenizer, BertForMaskedLM
from torch.utils.data import DataLoader, Dataset
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from torch.nn.utils.rnn import pad_sequence
from sklearn.decomposition import IncrementalPCA
import random
from torch.cuda.amp import autocast, GradScaler
from tqdm import tqdm 
import numpy as np


train_sentences = []
with open('/users/acp19hsy/Predictive TransformerTTS/Data/AAC Dataset/sent_train_aac.txt', 'r') as file:
    all_lines = file.readlines()
    num_lines_to_use = int(0.2 * len(all_lines))  # Calculate 20% of the total lines
    random_sample = random.sample(all_lines, num_lines_to_use)
    train_sentences = [line.strip() for line in random_sample]

# Step 2: Create masked sequences from the toy dataset
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
masked_train_sequences = []
mask_token_id = tokenizer.mask_token_id

for sentence in train_sentences:
    tokenized_sentence = tokenizer(sentence, return_tensors='pt', truncation=True)
    
    input_ids = tokenized_sentence['input_ids'].squeeze(0)
    attention_mask = tokenized_sentence['attention_mask'].squeeze(0)

    masked_indices = torch.rand(input_ids.shape) < 0.15
    masked_positions = torch.where(masked_indices & attention_mask)
    masked_sentence = input_ids.clone()
    masked_sentence[masked_positions] = mask_token_id

    masked_train_sequences.append(masked_sentence)


# Step 3: Create a custom dataset for masked language modeling (training dataset)
class TrainMLMCustomDataset(Dataset):
    def __init__(self, masked_sequences):
        self.masked_sequences = masked_sequences
    
    def __len__(self):
        return len(self.masked_sequences)
    
    def __getitem__(self, idx):
        masked_sequence = self.masked_sequences[idx]
        return {
            'input_ids': masked_sequence,
            'length': len(masked_sequence),
        }

    def collate_fn(self, batch):
            input_ids = [item['input_ids'] for item in batch]
            lengths = [item['length'] for item in batch]
            
            # Dynamically determine the maximum allowed length based on the longest sequence in the batch
            max_allowed_length = min(max(lengths), 8)  # You can adjust the maximum allowed length
            input_ids = [ids[:max_allowed_length] for ids in input_ids]

            # Dynamically pad sequences to the length of the longest sequence in the batch
            max_length = max(lengths)
            padded_input_ids = [torch.cat([ids, torch.zeros(max_length - len(ids))]) for ids in input_ids]
            
            return {
                'input_ids': torch.stack(padded_input_ids),
                'lengths': lengths
            }

train_mlm_dataset = TrainMLMCustomDataset(masked_train_sequences)
train_data_loader = DataLoader(train_mlm_dataset, batch_size=1, shuffle=True, collate_fn=train_mlm_dataset.collate_fn)

# Step 4: Prepare a toy test dataset
test_sentences = []
with open('/users/acp19hsy/Predictive TransformerTTS/Data/AAC Dataset/sent_test_aac.txt', 'r') as file:
    all_lines = file.readlines()
    num_lines_to_use = int(0.2 * len(all_lines))  # Calculate 20% of the total lines
    random_sample = random.sample(all_lines, num_lines_to_use)
    test_sentences = [line.strip() for line in random_sample]


# Step 5: Create tokenized sequences for the test dataset
class TestMLMCustomDataset(Dataset):
    def __init__(self, masked_sequences):
        self.masked_sequences = masked_sequences
    
    def __len__(self):
        return len(self.masked_sequences)
    
    def __getitem__(self, idx):
        masked_sequence = self.masked_sequences[idx]
        return {
            'input_ids': masked_sequence,
            'length': len(masked_sequence),
        }

    def collate_fn(self, batch):
        input_ids = [item['input_ids'] for item in batch]
        lengths = [item['length'] for item in batch]
        
        # Dynamically determine the maximum allowed length based on the longest sequence in the batch
        max_allowed_length = min(max(lengths), 8)  # You can adjust the maximum allowed length
        input_ids = [ids[:max_allowed_length] for ids in input_ids]

        # Dynamically pad sequences to the length of the longest sequence in the batch
        max_length = max(lengths)
        padded_input_ids = [torch.cat([ids, torch.zeros(max_length - len(ids))]) for ids in input_ids]
        
        return {
            'input_ids': torch.stack(padded_input_ids),
            'lengths': lengths
        }

# Load test sentences
test_sentences = []
with open('/users/acp19hsy/Predictive TransformerTTS/Data/AAC Dataset/sent_test_aac.txt', 'r') as file:
    all_lines = file.readlines()
    num_lines_to_use = int(1.0 * len(all_lines))  # Calculate 20% of the total lines
    random_sample = random.sample(all_lines, num_lines_to_use)
    test_sentences = [line.strip() for line in random_sample]

# Generate masked sequences for the test dataset
masked_test_sequences = []
mask_token_id = tokenizer.mask_token_id

for sentence in test_sentences:
    tokenized_sentence = tokenizer(sentence, return_tensors='pt', truncation=True)
    input_ids = tokenized_sentence['input_ids'].squeeze(0)
    attention_mask = tokenized_sentence['attention_mask'].squeeze(0)

    masked_indices = torch.rand(input_ids.shape) < 0.15
    masked_positions = torch.where(masked_indices & attention_mask)
    masked_sentence = input_ids.clone()
    masked_sentence[masked_positions] = mask_token_id

    masked_test_sequences.append(masked_sentence)

# Create test dataset and data loader
test_mlm_dataset = TestMLMCustomDataset(masked_test_sequences)
test_data_loader = DataLoader(test_mlm_dataset, batch_size=1, shuffle=False, collate_fn=test_mlm_dataset.collate_fn)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BertForMaskedLM.from_pretrained('bert-base-uncased').to(device)
training_losses_per_layer = []
training_accuracies_per_layer = []
test_accuracies_per_layer = []
test_accuracies_by_layer = []
training_losses_by_layer = []
layerwise_representations = []  # Store representations for each layer
original_state_dict = model.state_dict()

num_layers = model.config.num_hidden_layers
for layer_num in range(num_layers):
    layer_model = BertForMaskedLM.from_pretrained('bert-base-uncased').to(device)
    for param in layer_model.bert.encoder.layer[layer_num].parameters():
        param.requires_grad = False

    optimizer = torch.optim.Adam(layer_model.parameters(), lr=2e-5)
    criterion = torch.nn.CrossEntropyLoss()

    layer_model.train()
    num_epochs = 10
    epoch_losses = []  # Store losses for this epoch
    epoch_accuracies = []  # Store accuracies for this epoch
    for epoch in range(num_epochs):
        losses = []
        accuracies = []
        accumulation_steps = 4  # Accumulate gradients over 4 batches before updating weights
        scaler = GradScaler()
    
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        for batch_idx, batch in enumerate(train_data_loader):
            input_ids = batch['input_ids'].to(device, dtype=torch.long)
            labels = input_ids.clone()
            labels[input_ids == tokenizer.mask_token_id] = -100

            optimizer.zero_grad()
            
            with autocast():
                outputs = layer_model(input_ids=input_ids, labels=labels)
                loss = outputs.loss
            
            scaler.scale(loss).backward()
            
            if (batch_idx + 1) % accumulation_steps == 0:  # Update weights every accumulation_steps batches
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad()

            losses.append(loss.item())
            predictions = outputs.logits.argmax(dim=-1)
            accuracy = torch.sum(predictions == labels) / torch.sum(labels != -100)
            accuracies.append(accuracy.item())

        # If there are remaining accumulated gradients, update weights
        if (batch_idx + 1) % accumulation_steps != 0 or batch_idx == len(train_data_loader) - 1:
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad()

        epoch_losses.append(sum(losses) / len(losses))  # Average loss over batches in epoch
        epoch_accuracies.append(sum(accuracies) / len(accuracies))  # Average accuracy over batches in epoch

        print(f"Layer {layer_num}: Epoch {epoch + 1}, Average Training Loss: {epoch_losses[-1]:.4f}, Average Training Accuracy: {epoch_accuracies[-1]:.4f}") 

        # Extract hidden representations for the last epoch
        layer_model.eval()
        representations_for_layer = []
        with torch.no_grad():
            for batch in train_data_loader:
                input_ids = batch['input_ids'].to(device, dtype=torch.long)
                outputs = layer_model(input_ids=input_ids)
                representations_for_layer.append(outputs.logits.to('cpu'))

        # Ensure all tensors have the same number of examples by padding them
        representations_for_layer_padded = pad_sequence([rep.squeeze(0) for rep in representations_for_layer], batch_first=True, padding_value=0)

        representations_for_layer_combined = torch.cat([rep for rep in representations_for_layer_padded if rep.numel() > 0], dim=0)
        layerwise_representations.append(representations_for_layer_combined)

        # Calculate test accuracy for this layer after training
        layer_model.eval()
        with torch.no_grad():
            for batch in test_data_loader:
                input_ids = batch['input_ids'].to(device, dtype=torch.long)
                labels = input_ids.clone()
                labels[input_ids == tokenizer.mask_token_id] = -100  # Ignore loss for non-masked tokens

                outputs = layer_model(input_ids=input_ids, labels=labels)
                predictions = outputs.logits.argmax(dim=-1)
                accuracy = torch.sum(predictions == labels) / torch.sum(labels != -100)
                test_accuracies_per_layer.append(accuracy.item())

    training_losses_per_layer.append(epoch_losses)  # Store the losses for this layer all the epochs
    training_accuracies_per_layer.append(epoch_accuracies)  # Store the training accuracies for this layer for all the epochs
    average_test_accuracy = sum(epoch_accuracies) / num_epochs
    average_training_loss_per_layer=sum(epoch_losses) / num_epochs
    training_losses_by_layer.append(average_training_loss_per_layer)
    test_accuracies_by_layer.append(average_test_accuracy)

    print(f"Layer {layer_num}, Average Word Test Accuracy after Training: {average_test_accuracy:.4f}")
    print(f"Layer {layer_num}, Training losses by layer: {training_losses_by_layer}")
    print(f"Layer {layer_num}, Training losses per layer: {training_losses_per_layer}")

print('Training loss curve')
# Extract losses for each epoch from the nested list, handling potential float values
epoch_losses_per_layer = []
for layer in training_losses_per_layer:
    layer_losses = [epoch[0] if isinstance(epoch, list) else epoch for epoch in layer]
    epoch_losses_per_layer.append(layer_losses)
plt.figure(figsize=(10, 6))
for layer_num, epoch_losses in enumerate(epoch_losses_per_layer):
    plt.plot(range(1, len(epoch_losses) + 1), epoch_losses, label=f"Layer {layer_num}")
plt.title('Training Loss per Layer Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.legend()
plt.grid()
plt.savefig('Trainingloss.png')

# Plot test accuracy for each layer
print('Test word accuracy curves')
plt.figure(figsize=(10, 6))
plt.plot(test_accuracies_by_layer, marker='o')
plt.xticks(range(num_layers), [f'Layer {i}' for i in range(num_layers)])
plt.xlabel('Layer')
plt.ylabel('Average Test Accuracy')
plt.title('Average Word Accuracy for the Test Set per Layer')
plt.grid(True)
plt.savefig('TestAccuracy.png')

print('PCA STEP')
# Step 5: Reduce dimensionality with PCA
# Initialize variables
all_layerwise_representations = []
hidden_size = model.config.hidden_size

print('LAYER REPRESENTATIONS')
# Loop through each layer
for layer_num in range(num_layers):
    layer_representation = layerwise_representations[layer_num]
    all_layerwise_representations.append(layer_representation)

# Concatenate the representations from all layers
layerwise_representations_combined = torch.cat(all_layerwise_representations, dim=0)

# Flatten the combined representations
layerwise_representations_combined_flat = layerwise_representations_combined.view(layerwise_representations_combined.size(0), -1)

# Convert to float32 to reduce memory usage
layerwise_representations_combined_flat = layerwise_representations_combined_flat.to(torch.float32)

print('INCREMENTAL PCA')
n_components = 2  # Adjust the number of components
batch_size_incremental_pca = 2  # Adjust this based on memory availability
ipca = IncrementalPCA(n_components=n_components, batch_size=batch_size_incremental_pca)

# Create a tqdm progress bar for the Incremental PCA process
pca_result = []
batch_start = 0
total_batches = np.ceil(layerwise_representations_combined_flat.size(0) / batch_size_incremental_pca)
# Use tqdm to create a progress bar
for batch_num in tqdm(range(0, int(total_batches))):
    batch_end = min(batch_start + batch_size_incremental_pca, layerwise_representations_combined_flat.size(0))
    batch = layerwise_representations_combined_flat[batch_start:batch_end]
    ipca.partial_fit(batch)  # Fit the IncrementalPCA on the batch
    batch_start = batch_end
# Transform the entire data using the fitted IncrementalPCA
pca_result = ipca.transform(layerwise_representations_combined_flat)

# Step 6: Visualization with PCA
print('Visualisation with PCA')
for layer_num in range(num_layers):
    pca_result_layer = pca_result[layer_num * len(train_sentences): (layer_num + 1) * len(train_sentences)]
    
    plt.figure(figsize=(12, 8))
    plt.scatter(pca_result_layer[:, 0], pca_result_layer[:, 1])
    
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title(f'PCA Visualization of Training Layer {layer_num}')
    plt.savefig(f'pca_visualization_layer_{layer_num}.png')
    plt.close()  # Close the plot to release memory
