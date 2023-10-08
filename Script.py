import os
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import keras

folder_path = r'C:\Users\Shahab Kabiri\Dropbox\ThesisData\LSTMLogFiles'
output_file = 'history_data.xlsx'
output_path = os.path.join(folder_path, output_file)
combined_image_path = r'C:\Users\Shahab Kabiri\Dropbox\ThesisData\LSTMLogFiles\combined_charts.png'
text_file_path = r'C:\Users\Shahab Kabiri\Dropbox\ThesisData\LSTMLogFiles\Results.txt'  # Specify the path to your text file


r'C:\Users\Shahab Kabiri\Dropbox\ThesisData\LSTMLogFiles\3.history'


data = {}
for filename in os.listdir(folder_path):
    if filename.startswith('.'):  # Ignore hidden files
        continue
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # Extract the integer from the file name
        sheet_name = filename.split('-')[0]

        # Read the file using pickle
        with open(file_path, 'rb') as reader:
            history = pickle.load(reader)

        # Extract the required values from the history object
        loss = history.history['loss']
        val_loss = history.history['val_loss']
        # mae = history.history['mae']
        # val_mae = history.history['val_mae']

        # Create a DataFrame from the extracted values
        df = pd.DataFrame({'loss': loss, 'val_loss': val_loss})#, 'mae': mae, 'val_mae': val_mae})

        # Save the data in the dictionary
        data[sheet_name] = df

# Extract data from the text file and add it to the corresponding DataFrame
with open(text_file_path, 'r') as text_file:
    for line in text_file:
        line = line.strip()
        if line.startswith('.'):  # Ignore hidden lines
            continue
        # Extract the sheet name and epoch value from the line
        sheet_name, epoch_data = line.split('--', 0) , line.split('--', 1)
        epoch_value = epoch_data.split('Epoch(')[1].split(')')[0]
        # Extract the additional data after the epoch value
        additional_data = epoch_data.split(')')[1].strip()

        # Check if the sheet name exists in the data dictionary
        if sheet_name in data:
            # Add the epoch data to the corresponding DataFrame
            data[sheet_name]['epoch'] = int(epoch_value)
            data[sheet_name]['additional_data'] = additional_data

# Create a combined figure for all charts
fig, axs = plt.subplots(len(data), figsize=(10, 6 * len(data)))

# Plot each chart and add the sheet title as a label
for i, (sheet_name, df) in enumerate(data.items()):
    ax = axs[i]
    ax.plot(df['loss'], label='loss')
    ax.plot(df['val_loss'], label='val_loss')
    ax.set_xlabel('Epochs')
    ax.set_ylabel('Loss')
    ax.set_title(sheet_name)
    ax.legend()

    # Add the additional data as a text annotation
    annotation = df['additional_data'].iloc[-1]
    ax.annotate(annotation, xy=(1, df['val_loss'].iloc[-1]), xycoords='data',
                xytext=(10, 0), textcoords='offset points', fontsize=10)

# Adjust the layout and spacing between subplots
fig.tight_layout()

# Save the combined figure as a single image
fig.savefig(combined_image_path)

# Close the figure to free up memory
plt.close(fig)

# print(f"Combined chart image saved to: {combined_image_path}")
