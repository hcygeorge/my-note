# DevOps筆記

## 什麼是CI/CD?

### 持續整合(CI)
持續整合是最低限度的程式碼品質把關者。最低限度的意思是他只會做你要求的檢查。持續整合代表每次程式碼異動(commit)都會自動測試(自動化測試)，藉此幫助開發者提早發現並修復程式碼的問題。

持續整合流程  
code->build->test->release

CI七大要領
- commit code frequently
- don't commit broken code
- ...

### 持續交付(CD)
持續交付指的是任何人(環境)都可取得(部署)任一版本的應用程式(不只是source code)，有些專案會將production獨立於持續交付外，稱為持續部署。

持續交付流程  
交付: code->build->test->release->deploy(on dev or staging)->test  
部署: test->deploy(on production)  

## CI/CD Pipeline

- 第1代: 以VM+Jenkins(CI工具)打造CI/CD pipeline
- 第2代: Pipeline as Code，在YAML檔中設定CI/CD pipeline
- 第2.5代: 在container中執行CI/CD Pipeline工作
- 第3代: Everything as Code，所有東西的異動(code,infra,env)都以code操作，都能套用CI/CD流程


## 結論
1. 根據自己團隊特性決定導入第幾代CI/CD
2. 沒有做自動化測試，不要說你在做CI/CD

## 參考資料

ChengWeiChen在IT邦的DevOps系列文\
https://ithelp.ithome.com.tw/users/20120986/ironman/5646