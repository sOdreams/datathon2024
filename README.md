# Product Attribute Prediction Challenge

## Overview

This challenge focuses on building a model capable of predicting the design attributes of a product based on its **image** and **metadata**. The goal is to submit accurate predictions for each item's attributes, ensuring that invalid attributes are appropriately labeled.

---

## Objective

Participants must submit a two-column dataset in the following format:

| test_id   | des_value   |
|-----------|-------------|
| unique_id | prediction  |

Where:

- **test_id**: The unique identifier for each test row.
- **des_value**: The predicted value of the attribute `attribute_name` for the product `cod_modelo_color`.

Each item in the test set appears **11 times**, corresponding to 11 possible attribute types. The task requires predicting the correct `des_value` for each attribute of every item.

### Important Considerations

- **Not all attributes are applicable to every product.**
  For example:
  - Trousers do not have a `sleeve_length_type` attribute.
  - For such invalid attribute-item combinations, set `des_value` to `"INVALID"`.

---

## Data

Detailed information about the dataset can be found in the **Data** tab of the challenge platform. The data includes:

- **Product Images**: Visual representation of each product.
- **Product Metadata**: Additional information about the product (e.g., category, style, material, etc.).

The dataset is divided into:
- **Training Set**: For training your model.
- **Test Set**: For evaluating your predictions.

---

## Submission

Prepare a **CSV file** with the following structure:

| test_id   | des_value   |
|-----------|-------------|
| unique_id | prediction  |

- Each row corresponds to a combination of a product, an attribute, and its predicted value.
- Ensure that invalid attributes are labeled as `"INVALID"`.

---

## Evaluation

The challenge is evaluated using **accuracy** as the performance metric. Accuracy is defined as:

\[
\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Predictions}}
\]

Refer to the [scikit-learn accuracy score documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) for more details.

---

## How to Get Started

1. **Data Preprocessing**:
   - Load and clean the metadata.
   - Prepare and preprocess the product images (e.g., resizing, normalization).

2. **Model Development**:
   - Train a multi-input model combining image features and metadata.
   - Explore transfer learning for image processing and feature engineering for metadata.

3. **Prediction**:
   - Ensure predictions for valid attributes are accurate.
   - Set `"INVALID"` for invalid attribute-item combinations.

4. **Submission**:
   - Generate the output CSV in the required format.
   - Validate your predictions before submitting.

---

## Best Practices

- **Handle Invalid Cases**: Carefully map product types to applicable attributes to minimize incorrect predictions of `"INVALID"`.
- **Model Evaluation**: Use a validation set to monitor accuracy before submitting.
- **Feature Engineering**: Experiment with additional metadata-derived features and visual embeddings.

---

## Resources

- [scikit-learn documentation](https://scikit-learn.org/)
- [Image preprocessing with TensorFlow/Keras](https://www.tensorflow.org/tutorials/images)
- [CSV File Handling in Python](https://pandas.pydata.org/docs/)

