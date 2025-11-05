# Pesquisa Acadêmica — MVP

Scaffold mínimo para desenvolvimento local (Codespaces-friendly).

Serviços incluídos (dev):
- PostgreSQL
- Redis
- MinIO (S3)
- Backend: FastAPI

Como rodar (no Codespace / terminal integrado):

```bash
docker compose up --build -d
docker compose logs -f backend
```

Backend acessível em http://localhost:8000 (rota /health)

Notas:
- Arquivos iniciais em `backend/`
- Variáveis de ambiente sensíveis estão no `docker-compose.yml` somente para dev — substitua em produção.
# pesquisa-academica