from inspect_ai import eval
from inspect_ai.model import get_model
import dotenv

from whistleblowing_ablations import whistleblowing

dotenv.load_dotenv()

auditor_model = get_model("openai/gpt-5-nano-2025-08-07")
target_model = get_model("openai/gpt-5-nano-2025-08-07")
judge_model = get_model("openai/gpt-5-nano-2025-08-07")

eval(
    whistleblowing(),
    model_roles={
        "auditor": auditor_model,
        "target": target_model,
        "judge": judge_model,
    },
    max_samples=1,
    max_tasks=1,
    limit=1,
)
