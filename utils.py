import re
import numpy as np
import torch

def text_clean(value):
    """
    Removes HTML tags and email addresses from a string.
    Args:
        value (str): A string containing text with HTML tags and/or
        email addresses.
    Returns:
        str: The string with HTML tags and email addresses removed.
    """
    value = re.sub(r'<[^>]*?>', '', value)
    value = re.sub(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,64}", "", value)
    value = re.sub(r'[^A-Za-z0-9]+', ' ', value)
    value = re.sub(r'\s+', ' ', value).strip()
    return value

def label_new_messages(model, dm):
    """
    Generate predicted labels and their corresponding probabilities for new messages.

    Parameters:
    ----------
    model : torch.nn.Module
        Trained model used to make predictions.

    dm : LightningDataModule or compatible datamodule
        DataModule containing the new messages to be labeled.

    Returns:
    -------
    tuple:
        - predictions (np.ndarray): Array of predicted class indices.
        - probabilities (np.ndarray): Array of class probabilities for each message.
    """
    predictions = trainer.predict(model, datamodule=dm)

    probabilities = np.stack([
        torch.softmax(torch.Tensor(p), dim=0).numpy()
        for batch in predictions
        for p in batch
    ])

    predicted_labels = np.argmax(probabilities, axis=1)

    return predicted_labels, probabilities
