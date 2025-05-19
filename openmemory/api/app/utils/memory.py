import os

from mem0 import Memory


memory_client = None


def get_memory_client(custom_instructions: str = None, config_dict: dict = None):
    """
    Get or initialize the Mem0 client.

    Args:
        custom_instructions: Optional instructions for the memory project.
        config_dict: Optional configuration dictionary for Memory initialization.

    Returns:
        Initialized Mem0 client instance.

    Raises:
        Exception: If required API keys are not set.
    """
    global memory_client

    if memory_client is not None:
        return memory_client

    try:
    # 如果没有传入config_dict，使用默认配置
        if config_dict is None:
            config_dict = {
                "vector_store": {
                    "provider": "qdrant",
                    "config": {
                        "collection_name": "openmemory",
                        "host": "mem0_store",
                        "port": 6333,
                    }
                }
            }

        memory_client = Memory.from_config(config_dict)
    except Exception as e:
        raise Exception(f"Exception occurred while initializing memory client: {e}")

    # Update project with custom instructions if provided
    if custom_instructions:
        memory_client.update_project(custom_instructions=custom_instructions)

    return memory_client



def get_default_user_id():
    return "default_user"
