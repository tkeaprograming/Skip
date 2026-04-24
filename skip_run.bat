@echo off
:: 文字化け対策
chcp 65001 > nul
setlocal enabledelayedexpansion

:: --- 設定：tkx.py が置いてあるフルパス ---
set "SKIP_EXE=./skip.py"

:: 画面を一度きれいに
cls
echo --- Skip Interactive Runner ---
echo.

:: 引数（ドラッグ＆ドロップ）があるかチェック
if "%~1"=="" (
    set /p "target=実行したい .skp ファイルをここにドラッグ＆ドロップしてEnter: "
) else (
    set "target=%~1"
)

:: 入力されたパスから前後の引用符を確実に除去
set "target=!target:"=!"

:: 実行前に改行を入れて入力を安定させる
echo.
echo [Running: !target!]
echo ---------------------------------------
echo.

:: Python実行（tkx.pyとtargetの両方を引用符で囲んで安全に渡す）
python "%SKIP_EXE%" "!target!"

echo.
echo ---------------------------------------
echo 実行が終了しました。
pause
