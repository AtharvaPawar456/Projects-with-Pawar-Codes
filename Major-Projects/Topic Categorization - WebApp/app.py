from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the fine-tuned model
loaded_model = load_model("fine_tuned_text_classification_model.h5")

# Tokenizer setup
tokenizer = Tokenizer()

# Endpoint to classify text
@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data['text']
    
    # Convert test text to sequence and pad it
    test_sequences = tokenizer.texts_to_sequences([text])
    max_sequence_length = loaded_model.layers[0].input_length
    test_padded_sequences = pad_sequences(test_sequences, maxlen=max_sequence_length)
    
    # Perform inference
    predictions = loaded_model.predict(test_padded_sequences)
    predicted_label_index = np.argmax(predictions[0])
    
    return jsonify({"predicted_label": reverse_label_indices[predicted_label_index]})

if __name__ == '__main__':
    # Load tokenizer and reverse label indices here
    texts = [
        "Music is a universal language.",  # Add some example texts
        "Nature's beauty is unmatched.",
    ]
    tokenizer.fit_on_texts(texts)  # Use the same tokenizer as used during fine-tuning
    label_indices = {label: index for index, label in enumerate(set(labels))}
    reverse_label_indices = {index: label for label, index in label_indices.items()}
    
    app.run(debug=True)
