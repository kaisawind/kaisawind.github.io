# kaisawind.github.io

GitHub 仓库列表页（kaisawind / iotxfoundry / aixfoundry，含私有仓库），替代原 Hugo 博客。

[![Pages deploy](https://github.com/kaisawind/kaisawind.github.io/actions/workflows/static.yaml/badge.svg)](https://github.com/kaisawind/kaisawind.github.io/actions/workflows/static.yaml)
[![Netlify Status](https://api.netlify.com/api/v1/badges/c40090e1-18c5-484c-91b0-38d1bcae13c5/deploy-status)](https://app.netlify.com/sites/kaisawind/deploys)

## 更新页面

```sh
./generate.sh
git add index.html && git commit -m "refresh repo list" && git push
```

推送 master 后 Pages workflow（`.github/workflows/static.yaml`）自动部署。

注意：私有仓库名称、描述会公开出现在 https://kaisawind.github.io 上（已确认接受）。
