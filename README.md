# kaisawind.github.io

GitHub 仓库列表页（kaisawind / iotxfoundry / aixfoundry，含私有仓库），替代原 Hugo 博客。

## 更新页面

```sh
./generate.sh
git add index.html && git commit -m "refresh repo list" && git push
```

推送 master 后 Pages workflow（`.github/workflows/static.yaml`）自动部署。

注意：私有仓库名称、描述会公开出现在 https://kaisawind.github.io 上（已确认接受）。
