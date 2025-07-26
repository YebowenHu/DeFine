# DEFINE: Decision-Making with Analogical Reasoning over Factor Profiles
<div align="center">
  
[![arXiv](https://img.shields.io/badge/arXiv-2406.12084-b31b1b.svg?style=for-the-badge)](https://arxiv.org/abs/2406.12084) &nbsp;&nbsp;
[![Homepage](https://img.shields.io/badge/🏠-Homepage-blue?style=for-the-badge)](https://define-acl.github.io/) &nbsp;&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YebowenHu/DeFine) &nbsp;&nbsp;
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Datasets-yellow?style=for-the-badge)](https://huggingface.co/datasets/huuuyeah/DeFine)

</div>

This repository is dedicated to our research paper:  
**[DEFINE: Decision-Making with Analogical Reasoning over Factor Profiles](https://arxiv.org/abs/2410.01772)**  
(ACL 2025, July, Vienna, Austria)

## Abstract

LLMs are ideal for decision-making due to their ability to reason over long contexts and identify critical factors. However, challenges arise when processing transcripts of spoken speech describing complex scenarios. These transcripts often contain ungrammatical or incomplete sentences, repetitions, hedging, and vagueness. For example, during a company's earnings call, an executive might project a positive revenue outlook to reassure investors, despite significant uncertainty regarding future earnings. It is crucial for LLMs to incorporate this uncertainty systematically when making decisions. In this paper, we introduce DeFine, a new framework that constructs probabilistic factor profiles from complex scenarios. DeFine then integrates these profiles with analogical reasoning, leveraging insights from similar past experiences to guide LLMs in making critical decisions in novel situations. Our framework separates the tasks of quantifying uncertainty in complex scenarios and incorporating it into LLM decision-making. This approach is particularly useful in fields such as medical consultations, negotiations, and political debates, where making decisions under uncertainty is vital.

## Huggingface Datasets
We provide the all collected 11k earnings call transcripts and processed 1.6k factor profiles. The current analogical reasoning test cases retrieve the top-5 similar factor profiles from historical earnings call transcripts by kl-divergence. User can leverage the uploaded raw transcripts and factor profiles to test their own strategies to retrievel more accurate analogrical pair for decision making.

```
from datasets import load_dataset

test_set = load_dataset("huuuyeah/DeFine", "test", split='ar_top5')
ect_transcripts_all = load_dataset("huuuyeah/DeFine", "data", split='ect_transcripts')
ect_factor_profiles = load_dataset("huuuyeah/DeFine", "data", split='ect_fp')
```

## Citation

If you find this work useful, please consider citing our paper:

```bibtex
@misc{hu2024defineenhancingllmdecisionmaking,
      title={DeFine: Enhancing LLM Decision-Making with Factor Profiles and Analogical Reasoning}, 
      author={Yebowen Hu and Xiaoyang Wang and Wenlin Yao and Yiming Lu and Daoan Zhang and Hassan Foroosh and Dong Yu and Fei Liu},
      year={2024},
      eprint={2410.01772},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.01772}, 
}
