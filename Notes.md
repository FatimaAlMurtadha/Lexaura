# backend
cd Lexaura

git clone https://github.com/evrone/go-clean-template backend

cd backend
go mod edit -module github.com/FatimaAlMurtadha/Lexaura/backend
go mod tidy
rm -rf .git
cd ..

--------------------------------
# frontend
cd frontend

npx create-next-app@latest . --typescript

