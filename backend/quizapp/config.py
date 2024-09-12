from environs import Env

env = Env()
env.read_env()

mongo_uri = env.str("MONGO_URI")
mongo_test_uri = env.str("MONGO_URI")
