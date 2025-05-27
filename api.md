# Authorization

Types:

```python
from ambient_sdk.types import AuthorizationRetrieveResponse
```

Methods:

- <code title="get /authorization">client.authorization.<a href="./src/ambient_sdk/resources/authorization.py">retrieve</a>() -> str</code>

# Employee

Types:

```python
from ambient_sdk.types import (
    Employee,
    EmployeeCore,
    EmployeeCreateResponse,
    EmployeeUpdateResponse,
    EmployeeArchiveResponse,
    EmployeeBatchCreateResponse,
    EmployeeGetPaymentMethodsResponse,
    EmployeeGetTransactionsResponse,
    EmployeeUnarchiveResponse,
)
```

Methods:

- <code title="post /employee">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">create</a>(\*\*<a href="src/ambient_sdk/types/employee_create_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employee_create_response.py">EmployeeCreateResponse</a></code>
- <code title="get /employee/{idType}/{id}">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">retrieve</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employee/employee.py">Employee</a></code>
- <code title="post /employee/{idType}/{id}">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">update</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/employee_update_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employee_update_response.py">EmployeeUpdateResponse</a></code>
- <code title="post /employee/{idType}/{id}/archive">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">archive</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/employee_archive_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employee_archive_response.py">EmployeeArchiveResponse</a></code>
- <code title="post /employee/batch">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">batch_create</a>(\*\*<a href="src/ambient_sdk/types/employee_batch_create_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employee_batch_create_response.py">EmployeeBatchCreateResponse</a></code>
- <code title="get /employee/{idType}/{id}/payment-methods">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">get_payment_methods</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employee_get_payment_methods_response.py">EmployeeGetPaymentMethodsResponse</a></code>
- <code title="get /employee/{idType}/{id}/transaction">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">get_transactions</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/employee_get_transactions_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employee_get_transactions_response.py">EmployeeGetTransactionsResponse</a></code>
- <code title="post /employee/{idType}/{id}/unarchive">client.employee.<a href="./src/ambient_sdk/resources/employee/employee.py">unarchive</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employee_unarchive_response.py">EmployeeUnarchiveResponse</a></code>

## Balance

Types:

```python
from ambient_sdk.types.employee import BalanceRetrieveResponse, BalanceUpdateResponse
```

Methods:

- <code title="get /employee/{idType}/{id}/balance">client.employee.balance.<a href="./src/ambient_sdk/resources/employee/balance.py">retrieve</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employee/balance_retrieve_response.py">BalanceRetrieveResponse</a></code>
- <code title="post /employee/{idType}/{id}/balance">client.employee.balance.<a href="./src/ambient_sdk/resources/employee/balance.py">update</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/employee/balance_update_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employee/balance_update_response.py">BalanceUpdateResponse</a></code>

# Employer

Types:

```python
from ambient_sdk.types import (
    EmployerCore,
    EmployerCreateResponse,
    EmployerRetrieveResponse,
    EmployerUpdateResponse,
    EmployerCreateBatchResponse,
    EmployerListTransactionsResponse,
    EmployerRetrieveBalanceResponse,
    EmployerRetrieveBankInfoResponse,
)
```

Methods:

- <code title="post /employer">client.employer.<a href="./src/ambient_sdk/resources/employer.py">create</a>(\*\*<a href="src/ambient_sdk/types/employer_create_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employer_create_response.py">EmployerCreateResponse</a></code>
- <code title="get /employer/{idType}/{id}">client.employer.<a href="./src/ambient_sdk/resources/employer.py">retrieve</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employer_retrieve_response.py">EmployerRetrieveResponse</a></code>
- <code title="post /employer/{idType}/{id}">client.employer.<a href="./src/ambient_sdk/resources/employer.py">update</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/employer_update_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employer_update_response.py">EmployerUpdateResponse</a></code>
- <code title="post /employer/batch">client.employer.<a href="./src/ambient_sdk/resources/employer.py">create_batch</a>(\*\*<a href="src/ambient_sdk/types/employer_create_batch_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employer_create_batch_response.py">EmployerCreateBatchResponse</a></code>
- <code title="get /employer/{idType}/{id}/transaction">client.employer.<a href="./src/ambient_sdk/resources/employer.py">list_transactions</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/employer_list_transactions_params.py">params</a>) -> <a href="./src/ambient_sdk/types/employer_list_transactions_response.py">EmployerListTransactionsResponse</a></code>
- <code title="get /employer/{idType}/{id}/balance">client.employer.<a href="./src/ambient_sdk/resources/employer.py">retrieve_balance</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employer_retrieve_balance_response.py">EmployerRetrieveBalanceResponse</a></code>
- <code title="get /employer/{idType}/{id}/bank">client.employer.<a href="./src/ambient_sdk/resources/employer.py">retrieve_bank_info</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/employer_retrieve_bank_info_response.py">EmployerRetrieveBankInfoResponse</a></code>

# Health

Types:

```python
from ambient_sdk.types import HealthRetrieveStatusResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/ambient_sdk/resources/health.py">retrieve_status</a>() -> <a href="./src/ambient_sdk/types/health_retrieve_status_response.py">HealthRetrieveStatusResponse</a></code>

# Org

Types:

```python
from ambient_sdk.types import (
    Org,
    OrgCore,
    OrgCreateResponse,
    OrgUpdateResponse,
    OrgListTransactionsResponse,
    OrgRetrieveBalanceResponse,
    OrgRetrieveBankInfoResponse,
)
```

Methods:

- <code title="post /org">client.org.<a href="./src/ambient_sdk/resources/org/org.py">create</a>(\*\*<a href="src/ambient_sdk/types/org_create_params.py">params</a>) -> <a href="./src/ambient_sdk/types/org_create_response.py">OrgCreateResponse</a></code>
- <code title="get /org/{idType}/{id}">client.org.<a href="./src/ambient_sdk/resources/org/org.py">retrieve</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/org/org.py">Org</a></code>
- <code title="post /org/{idType}/{id}">client.org.<a href="./src/ambient_sdk/resources/org/org.py">update</a>(path_id, \*, id_type, \*\*<a href="src/ambient_sdk/types/org_update_params.py">params</a>) -> <a href="./src/ambient_sdk/types/org_update_response.py">OrgUpdateResponse</a></code>
- <code title="get /org/{idType}/{id}/transaction">client.org.<a href="./src/ambient_sdk/resources/org/org.py">list_transactions</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/org_list_transactions_params.py">params</a>) -> <a href="./src/ambient_sdk/types/org_list_transactions_response.py">OrgListTransactionsResponse</a></code>
- <code title="get /org/{idType}/{id}/balance">client.org.<a href="./src/ambient_sdk/resources/org/org.py">retrieve_balance</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/org_retrieve_balance_response.py">OrgRetrieveBalanceResponse</a></code>
- <code title="get /org/{idType}/{id}/bank">client.org.<a href="./src/ambient_sdk/resources/org/org.py">retrieve_bank_info</a>(id, \*, id_type) -> <a href="./src/ambient_sdk/types/org_retrieve_bank_info_response.py">OrgRetrieveBankInfoResponse</a></code>

## Employee

### PaymentMethods

Types:

```python
from ambient_sdk.types.org.employee import PaymentMethodListResponse
```

Methods:

- <code title="get /org/{idType}/{id}/employee/payment-methods/batch">client.org.employee.payment_methods.<a href="./src/ambient_sdk/resources/org/employee/payment_methods.py">list</a>(id, \*, id_type, \*\*<a href="src/ambient_sdk/types/org/employee/payment_method_list_params.py">params</a>) -> <a href="./src/ambient_sdk/types/org/employee/payment_method_list_response.py">PaymentMethodListResponse</a></code>

# Report

Types:

```python
from ambient_sdk.types import (
    ReportRetrieveArchivedAccountsReportResponse,
    ReportRetrieveFundingTransferDetailReportResponse,
    ReportRetrieveNonzeroBalanceAccountsReportResponse,
    ReportRetrievePaymentsReportResponse,
)
```

Methods:

- <code title="get /report/archived">client.report.<a href="./src/ambient_sdk/resources/report.py">retrieve_archived_accounts_report</a>(\*\*<a href="src/ambient_sdk/types/report_retrieve_archived_accounts_report_params.py">params</a>) -> <a href="./src/ambient_sdk/types/report_retrieve_archived_accounts_report_response.py">ReportRetrieveArchivedAccountsReportResponse</a></code>
- <code title="get /report/funding">client.report.<a href="./src/ambient_sdk/resources/report.py">retrieve_funding_transfer_detail_report</a>(\*\*<a href="src/ambient_sdk/types/report_retrieve_funding_transfer_detail_report_params.py">params</a>) -> <a href="./src/ambient_sdk/types/report_retrieve_funding_transfer_detail_report_response.py">ReportRetrieveFundingTransferDetailReportResponse</a></code>
- <code title="get /report/nonzero">client.report.<a href="./src/ambient_sdk/resources/report.py">retrieve_nonzero_balance_accounts_report</a>(\*\*<a href="src/ambient_sdk/types/report_retrieve_nonzero_balance_accounts_report_params.py">params</a>) -> <a href="./src/ambient_sdk/types/report_retrieve_nonzero_balance_accounts_report_response.py">ReportRetrieveNonzeroBalanceAccountsReportResponse</a></code>
- <code title="get /report/payments">client.report.<a href="./src/ambient_sdk/resources/report.py">retrieve_payments_report</a>(\*\*<a href="src/ambient_sdk/types/report_retrieve_payments_report_params.py">params</a>) -> <a href="./src/ambient_sdk/types/report_retrieve_payments_report_response.py">ReportRetrievePaymentsReportResponse</a></code>

# Transaction

Types:

```python
from ambient_sdk.types import (
    QueueTransaction,
    TransactionRetrieveResponse,
    TransactionBatchQueueResponse,
)
```

Methods:

- <code title="get /transaction/id/{id}">client.transaction.<a href="./src/ambient_sdk/resources/transaction.py">retrieve</a>(id) -> <a href="./src/ambient_sdk/types/transaction_retrieve_response.py">TransactionRetrieveResponse</a></code>
- <code title="post /transaction/batch">client.transaction.<a href="./src/ambient_sdk/resources/transaction.py">batch_queue</a>(\*\*<a href="src/ambient_sdk/types/transaction_batch_queue_params.py">params</a>) -> <a href="./src/ambient_sdk/types/transaction_batch_queue_response.py">TransactionBatchQueueResponse</a></code>
- <code title="post /transaction">client.transaction.<a href="./src/ambient_sdk/resources/transaction.py">queue</a>(\*\*<a href="src/ambient_sdk/types/transaction_queue_params.py">params</a>) -> <a href="./src/ambient_sdk/types/queue_transaction.py">QueueTransaction</a></code>
