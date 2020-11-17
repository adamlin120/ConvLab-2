# Environment

Please use `dev.dockerfile` or `install.sh` to install required packages for BOTH END2END and DST evaluation.

We use `transformers==3.2.0` in crosswoz-dst and multiwoz-dst.

Thank you!

# End2End

## Download
Please download the code and model by
```bash
bash download_end2end.sh
```
before evaluating.

## Evaluation

* automatic evaluation
```python automatic.py```

* human evaluation
```python human.py```


# XLDST

## Download

Our models are uploaded to [huggingface model hub](https://huggingface.co/ytlin), and are loaded in the codes by `Mode.from_pretrained(CHECKPOINT_NAME)`.


## Evaluation

### Public Test Set Prediction
predictions on `dstc9-test-250` are at
```
multiwoz-dst/
    submission1/
        submission1.json
    submission2/
        submission2.json
    submission3/
        submission3.json
    submission4/
        submission4.json
    submission5/
        submission5.json
crosswoz-dst/
    submission1/
        submission1.json
    submission2/
        submission2.json
    submission3/
        submission3.json
    submission4/
        submission4.json
    submission5/
        submission5.json
```

### Evaluate Model
Load model by 
```python
from multiwoz-dst.submission1 import Model
from multiwoz-dst.submission2 import Model
from multiwoz-dst.submission3 import Model
from multiwoz-dst.submission4 import Model
from multiwoz-dst.submission5 import Model
from crosswoz-dst.submission1 import Model
from crosswoz-dst.submission2 import Model
from crosswoz-dst.submission3 import Model
from crosswoz-dst.submission4 import Model
from crosswoz-dst.submission5 import Model
```


Please contact Yen-Ting, Lin (r08944064@csie.ntu.edu.tw) if you have any problem.