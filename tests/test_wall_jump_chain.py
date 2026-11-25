import pytest
import gameplay.wall_jump_chain as mod

CASES = [
    ("merge_normals_per_substep", (1,)),
    ("buffer_time_based", (1,)),
    ("wall_probe_hysteresis", (1,)),
    ("impulse_decay", (1,)),
    ("anim_normalized_time", (1,)),
    ("chain_count_cap", (1,)),
    ("attach", (1,)),
    ("jump", (1,)),
    ("chain", (1,)),
    ("present", (1,)),
    ("validate_walljump", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
