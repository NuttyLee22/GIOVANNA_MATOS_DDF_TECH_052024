import os, datetime
import subprocess
import pandas as pd
from great_expectations import Context, ExpectationSuite, BatchRequest

# Caminho para o arquivo de configuracao YAML
config_file_path = "config.yml"

# Instalar Great Expectations
if not os.path.exists("great_expectations"):
    subprocess.run(["pip", "install", "great_expectations"])

# Carregar Configuracoes
context = Context(config_root_dir=".")  # Update if config root is different

# Carregar dados
data = {}
for source in context.list_expectation_suites():
    suite = context.load_expectation_suite(source)
    validation_config = suite.to_yaml_dict()["validations"]
    for validation in validation_config:
        data_source_name = validation.get("kwargs", {}).get("data_asset")
        data[data_source_name] = pd.read_csv(data_source_name)

# Validar dados
batch_request = BatchRequest()
for source_name, source_data in data.items():
    batch_request.add_datasource(BatchRequest.Datasource(
        source_name=source_name,
        data=source_data
    ))

validation_result = context.run_validation_operator(batch_request)

# Gerar Relatorio
report_data = {
    "data_sources": list(data.keys()),
    "checks": validation_result.expectation_suite_validation_results[0].meta.expectation_suite_name,
    "results": {},
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

for expectation in validation_result.expectation_suite_validation_results[0].results:
    source_name = expectation.expectation_config.kwargs.get("data_asset")
    report_data["results"].setdefault(source_name, []).append({
        "expectation_id": expectation.expectation_config.kwargs.get("expectation_type"),
        "column": expectation.expectation_config.kwargs.get("column"),
        "result": expectation.success,
    })

report_path = "great_expectations_report_" + report_data["timestamp"] + ".csv"
with open(report_path, "w") as f:
    f.write("Data Source,Expectation ID,Column,Result\n")
    for source_name, source_results in report_data["results"].items():
        for result in source_results:
            f.write(f"{source_name},{result['expectation_id']},{result['column']},{result['result']}\n")

# Printa caminho do relatorio
print(f"Report generated at: {report_path}")
