from dotmap import DotMap

#####################
# HYPER-PARAMS
#####################
hyper_params = DotMap(dict(
    NUM_EPOCHS=150,
    BATCH_SIZE=32,
    IMG_INPUT_SIZE=256,
    PENCIL_STYLE="sketch",
    OPTIMIZER="Adam",
    LEARNING_RATE=2e-4,
    BETA_1=0.5,
    BETA_2=0.999,
))

#############################
# EVALUATION VISUALIZATION
############################
IMAGE_DISPLAY_VERBOSE = 4

########################
# Loss function params
#######################
LAMBDA_PARAM = 100

########################
# SAVINGS
#######################
save_generator = True
generator_filename = "generator_1"
