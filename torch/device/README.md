- A frequently used dynamic device assignment:
  `device = torch.device("cuda" if torch.cuda.is_available() else "cpu")`
- To move an entire model to some device: `model.to(device)`
    - No need to `model = model.to(device)` because it's inplace already
    - To check whether the model has been successfully moved to device:
      `next(model.parameters()).device`
