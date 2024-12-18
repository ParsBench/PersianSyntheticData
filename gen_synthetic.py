import json
import os
from dotenv import load_dotenv

load_dotenv()

from promptwright import DataEngine, EngineArguments, TopicTree, TopicTreeArguments

def generate_dataset(
    topic,
    system_prompt,
    instructions,
    tree_degree=7,
    tree_depth=4,
    num_steps=10,
    batch_size=1,
):
    tree = TopicTree(
        args=TopicTreeArguments(
            root_prompt=topic,
            model_system_prompt=system_prompt,
            tree_degree=tree_degree,
            tree_depth=tree_depth,
            temperature=0.7,
            model_name="openai/gpt-4o",
        )
    )

    tree.build_tree()
    tree.save(f"topic_trees/{topic}_tree.jsonl")

    engine = DataEngine(
        args=EngineArguments(
            instructions=instructions,
            system_prompt=system_prompt,
            model_name="openai/gpt-4o",
            temperature=0.1,
            max_retries=3,
        )
    )

    dataset = engine.create_data(
        num_steps=num_steps,
        batch_size=batch_size,
        topic_tree=tree,
        sys_msg=False,
    )

    dataset.save(f"datasets/{topic}_dataset.jsonl")


def load_prompts(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    prompts = load_prompts("prompts/topic_prompts.json")
    for prompt in prompts:
        if os.path.exists(f"datasets/{prompt['موضوع']}_dataset.jsonl"):
            print(f"Skipping {prompt['موضوع']} because it already exists")
            continue
        generate_dataset(prompt["موضوع"], prompt["نقش"], prompt["دستورالعمل"])

if __name__ == "__main__":
    main()
