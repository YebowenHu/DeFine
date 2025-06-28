# DEFINE: Decision-Making with Analogical Reasoning over Factor Profiles

This repository is dedicated to our research paper:  
**[DEFINE: Decision-Making with Analogical Reasoning over Factor Profiles](https://arxiv.org/abs/2410.01772)**  
(ACL 2025, July, Vienna, Austria)

## Abstract

LLMs are ideal for decision-making due to their ability to reason over long contexts and identify critical factors. However, challenges arise when processing transcripts of spoken speech describing complex scenarios. These transcripts often contain ungrammatical or incomplete sentences, repetitions, hedging, and vagueness. For example, during a company's earnings call, an executive might project a positive revenue outlook to reassure investors, despite significant uncertainty regarding future earnings. It is crucial for LLMs to incorporate this uncertainty systematically when making decisions. In this paper, we introduce DeFine, a new framework that constructs probabilistic factor profiles from complex scenarios. DeFine then integrates these profiles with analogical reasoning, leveraging insights from similar past experiences to guide LLMs in making critical decisions in novel situations. Our framework separates the tasks of quantifying uncertainty in complex scenarios and incorporating it into LLM decision-making. This approach is particularly useful in fields such as medical consultations, negotiations, and political debates, where making decisions under uncertainty is vital.

## Coming Soon
- **Tools:** Analogical Prompt Template, Evaluation tool set.
- **Dataset:** Factor Profiles extracted from 1,100 earnings call transcripts, Experimental Results. 

All resources will be released publicly upon official publication.  
Please star ⭐ the repo to get updates!

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
