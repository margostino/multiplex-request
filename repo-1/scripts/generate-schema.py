if __name__ == '__main__':
    # create a json schema from a yaml file
    import yaml
    import json

    with open("repo-1/metadata.yml", 'r') as file:
        metadata = yaml.safe_load(file)
        with open("repo-1/schema.json", 'w') as file:
            json.dump(metadata['request'], file, indent=4)

    print("new schema generated")
