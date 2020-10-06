"""
    evaluate DST model
"""

import json
import importlib
from argparse import ArgumentParser

from tqdm.auto import tqdm

from convlab2.dst import DST
from convlab2.dst.dstc9.utils import prepare_data, eval_states


def evaluate(model_dir, subtask, test_data, gt):
    module = importlib.import_module(f"{subtask}-dst.{model_dir}")
    assert "Model" in dir(
        module
    ), "please import your model as name `Model` in your subtask module root"
    model_cls = module.__getattribute__("Model")
    assert issubclass(model_cls, DST), "the model must implement DST interface"
    # load weights, set eval() on default
    model = model_cls()
    pred = {}
    ana = {}
    for dialog_id, turns in tqdm(test_data.items()):
        model.init_session()
        pred[dialog_id] = []
        for i, (sys_utt, user_utt, gt_turn) in enumerate(turns):
            pred_turn = model.update_turn(sys_utt, user_utt)
            pred[dialog_id].append(pred_turn)

            # diff = {
            #     domain: {
            #         slot_name: {"gt": slot_value, "pred": pred_turn[domain][slot_name]}
            #         for slot_name, slot_value in domain_slots.items()
            #         if slot_value != pred_turn[domain][slot_name]
            #     }
            #     for domain, domain_slots in gt_turn.items()
            # }
            # clean_diff = {k: v for k, v in diff.items() if v}
            # ana[f"{dialog_id}-{i}"] = clean_diff
            # pprint(clean_diff)

        # pred[dialog_id] = [
        #     model.update_turn(sys_utt, user_utt) for sys_utt, user_utt, gt_turn in turns
        # ]
        # result = eval_states(gt, pred, subtask)
        # print(json.dumps(result, indent=4, ensure_ascii=False))

    json.dump(
        pred,
        open(f"./{subtask}-dst/{model_dir}/pred_{args.split}.json", "w"),
        indent=4,
        ensure_ascii=False,
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("subtask", type=str, choices=["multiwoz", "crosswoz"])
    parser.add_argument(
        "split",
        type=str,
        choices=["train", "val", "test", "human_val", "dstc9-test-250"],
    )
    parser.add_argument(
        "submission", type=str, choices=[f"submission{i}" for i in range(1, 6)]
    )
    args = parser.parse_args()
    subtask = args.subtask
    test_data = prepare_data(subtask, args.split)
    gt = {
        dialog_id: [state for _, _, state in turns]
        for dialog_id, turns in test_data.items()
    }
    evaluate(args.submission, subtask, test_data, gt)
