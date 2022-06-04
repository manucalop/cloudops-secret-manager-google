from cloudops_google_secretmanager import SecretManager

your_secret_manager = SecretManager("porject_id", "secret_id")

# Get the latest version of your secret
your_secret = your_secret_manager.pull()

# Modify it
your_secret["new_value"] = "foo"

# Push a new version of your secret
your_secret_manager.push(your_secret)
