Este é um projeto para a demonstração do uso da Z-API integrada a um back-end Supabase para o processo seletivo da b2bflow.

## Arquitetura
- Entrada: CLI via Docker
- Integração: Z-API
- Persistência: Supabase

## Requisitos
- Docker instalado
- Z-API com instância configurada e conectada
- Projeto Supabase com tabela configurada da seguinte forma:

| Column     | Type                        | Nullable | Default  | Constraints      |
|------------|-----------------------------|----------|----------|------------------|
| id         | bigint                      | no       | identity | primary key      |
| created_at | timestamp with time zone    | no       | now()    |                  |
| name       | text                        | yes      | -        |                  |
| number     | text                        | yes      | -        |                  |

## Instalação
1. Clone o projeto
```cmd
git clone https://github.com/Natan822/b2bflow-zapi
cd b2bflow-zapi
```

2. Configure as variáveis de ambiente

Renomeie o arquivo `.env.template` para `.env` e preencha com os seguintes valores:
- **SUPABASE_URL**: URL base do projeto Supabase (Ex.: https://exemplo.supabase.co)
- **SUPABASE_KEY**: Secret key do Supabase
- **SUPABASE_TABLE_NAME**: Nome da tabela de contatos no Supabase
- **ZAPI_INSTANCE_ID**: ID da sua instância, obtido no painel da Z-API
- **ZAPI_INSTANCE_TOKEN**: Token da sua instância, obtido no painel da Z-API
- **ZAPI_CLIENT_TOKEN**: Token de segurança da conta


3. Gere a imagem Docker:
```cmd
docker build -t b2bflow-zapi .
```

## Como usar
Com o projeto já instalado:
1. Execute a imagem Docker gerada:
```cmd
docker run --env-file .env -it b2bflow-zapi
```
2. Siga as instruções exibidas no terminal para a seleção dos destinatários das mensagens.