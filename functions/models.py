def models(unprinted_models, printed_models):
    """Simulate printing of 3D designs
    then move each completed design to printed models"""
    while unprinted_models:
        current_print = unprinted_models.pop()
        print("Currently printing:" + current_print)
        printed_models.append(current_print)

def completed_models(printed_models):
    """Show all models that were printed."""
    print("The following models are completed:")
    for printed_model in printed_models:
        print(printed_model)

unprinted_models = ['iphone case', 'hectagon', 'toy car', 'figurine']
printed_models = []

models(unprinted_models, printed_models)
completed_models(printed_models)
