from hydra import initialize, compose


def main():
    with initialize(config_path="../conf", version_base="1.3"):
        cfg = compose(config_name="config.yaml")
    if cfg.llms.name == "banana_dev":
        return
