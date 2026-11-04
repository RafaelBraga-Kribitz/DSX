: << 'CMDBLOCK'
@echo off
REM Cross-platform polyglot wrapper for hook scripts.
REM On Windows: cmd.exe runs this batch portion, which finds bash and hands over.
REM On Unix: the shell interprets the file as a script (":" is a no-op in bash,
REM so the whole batch block is a quoted heredoc that bash skips).
REM
REM Hook scripts use extensionless names ("stop-gate", not "stop-gate.sh") so
REM Claude Code's Windows auto-detection, which prepends "bash" to any command
REM containing ".sh", does not interfere.
REM
REM Usage: run-hook.cmd <script-name> [args...]

if "%~1"=="" (
    echo run-hook.cmd: missing script name >&2
    exit /b 1
)

set "HOOK_DIR=%~dp0"

if exist "C:\Program Files\Git\bin\bash.exe" (
    "C:\Program Files\Git\bin\bash.exe" "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)
if exist "C:\Program Files (x86)\Git\bin\bash.exe" (
    "C:\Program Files (x86)\Git\bin\bash.exe" "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)

where bash >nul 2>nul
if %ERRORLEVEL%==0 (
    bash "%HOOK_DIR%%~1" %2 %3 %4 %5 %6 %7 %8 %9
    exit /b %ERRORLEVEL%
)

echo run-hook.cmd: bash not found. Install Git for Windows. >&2
exit /b 1
CMDBLOCK

# ── Unix ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [ -z "${1:-}" ]; then
  echo "run-hook.cmd: missing script name" >&2
  exit 1
fi
name="$1"
shift
exec bash "$SCRIPT_DIR/$name" "$@"
