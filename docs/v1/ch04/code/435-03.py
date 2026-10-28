predicted_index = np.argmax(probabilities)
predicted_class = classes[predicted_index]
shifted_again = scores + 100.0
shifted_again = shifted_again - shifted_again.max()
probabilities_again = np.exp(shifted_again)
probabilities_again = probabilities_again / probabilities_again.sum()
print('predicted index:', predicted_index)
print('predicted class:', predicted_class)
print('same probabilities:', np.allclose(probabilities, probabilities_again))
