Python CLI listing available Azure ML Compute quotas across regions as CSV

Install dependencies (using Conda -- [miniconda](https://docs.conda.io/en/latest/miniconda.html) is sufficient):
```
conda create -y -n amlquota python=3.9
conda activate amlquota
pip install requests==2.27.1 azure-identity==1.10.0
```

Syntax:
```bash
python3 list_aml_compute_quotas.py subscription_id
```

Example:
```bash
python3 list_aml_compute_quotas.py 12345678-1234-1234-1234-123456789abc
```

Output:
```
region,available,current,limit,name
eastus,200,0,200,TotalClusters
eastus,100,0,100,TotalDedicatedCores
eastus,100,0,100,standardDFamily
eastus,100,0,100,standardDv2Family
...
```