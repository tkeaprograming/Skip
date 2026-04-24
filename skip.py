import yaml
import sys
import os
import random
import time

class C:
    R, G, Y, B, END = "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[0m"

class SkipCommand:
    def __init__(self, interpreter):
        self.interp = interpreter

    def _f(self, value):
        if not isinstance(value, str): return value
        try:
            return eval(f'f"{value}"', {"C": C, "random": random, "time": time}, self.interp.vars)
        except: return value

    def println(self, value): print(self._f(value))

    def typetext(self, value):
        text = self._f(value)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)
        print()

    def var(self, value):
        if isinstance(value, dict):
            for k, v in value.items(): self.interp.vars[k] = self._f(v)

    def clc(self, value):
        try:
            expr = value.get("val") if isinstance(value, dict) else value
            res = eval(str(expr), {"random": random, "time": time}, self.interp.vars)
            self.interp.vars['res'] = res
            if not (isinstance(value, dict) and value.get("silent")): print(res)
        except Exception as e: print(f"{C.R}[Calc Error] {e}{C.END}")

    def input(self, value):
        var_name = str(value)
        sys.stdout.flush()
        user_input = input(f"{var_name} >> ")
        try:
            if "." in user_input: self.interp.vars[var_name] = float(user_input)
            else: self.interp.vars[var_name] = int(user_input)
        except: self.interp.vars[var_name] = user_input

    def wait(self, value):
        try: time.sleep(float(self._f(value)))
        except: pass

    def if_cmd(self, value):
        try:
            is_true = eval(str(value.get("cond", "False")), {"C": C, "random": random, "time": time}, self.interp.vars)
            self.interp.execute_block(value.get("then", []) if is_true else value.get("else", []))
        except Exception as e: print(f"{C.R}[IF Error] {e}{C.END}")

    def loop(self, value):
        try:
            for i in range(int(self._f(value.get("count", 0)))):
                self.interp.vars["_i"] = i + 1
                self.interp.execute_block(value.get("do", []))
        except Exception as e: print(f"{C.R}[Loop Error] {e}{C.END}")

    def importxt(self, value):
        filename = self._f(value)
        if not filename.endswith(".tkx"): filename += ".tkx"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if data: self.interp.execute_block(data)
        else: print(f"{C.R}[Import Error] {filename} not found{C.END}")

    def savext(self, value):
        if not isinstance(value, dict): return
        filename = self._f(value.get("file", "save.tkx"))
        target_vars = value.get("vars", [])
        save_data = [{"var": {v: self.interp.vars[v]}} for v in target_vars if v in self.interp.vars]
        with open(filename, 'w', encoding='utf-8') as f:
            yaml.dump(save_data, f, allow_unicode=True, default_flow_style=False)
        print(f"{C.G}[Saved] -> {filename}{C.END}")

    # --- 新機能: def と call ---
    def def_cmd(self, value):
        """関数を定義する (def: { name: '関数名', do: [命令] })"""
        if not isinstance(value, dict): return
        func_name = value.get("name")
        func_body = value.get("do", [])
        self.interp.funcs[func_name] = func_body

    def call(self, value):
        """定義した関数を呼び出す (call: '関数名')"""
        func_name = self._f(value)
        if func_name in self.interp.funcs:
            self.interp.execute_block(self.interp.funcs[func_name])
        else:
            print(f"{C.R}[Call Error] 関数 '{func_name}' は定義されていません{C.END}")

    def exit(self, value):
        if value: self.typext(value)
        sys.exit()

class SkipInterpreter:
    def __init__(self):
        self.vars = {"res": 0}
        self.funcs = {} # 関数保存用
        self.cmd_executor = SkipCommand(self)

    def run(self, argv):
        if len(argv) < 2: return
        path = argv[1].strip('"')
        if not os.path.exists(path):
            print(f"Error: {path} not found")
            return
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data: self.execute_block(data)

    def execute_block(self, commands):
        target = commands if isinstance(commands, list) else [commands]
        for step in target:
            if isinstance(step, dict):
                for k, v in step.items(): self.dispatch(k, v)

    def dispatch(self, k, v):
        c = self.cmd_executor
        cmds = {
            "println":c.println, "typetext":c.typetext, "var":c.var, "clc":c.clc, 
            "input":c.input, "wait":c.wait, "if":c.if_cmd, "loop":c.loop, 
            "exit":c.exit, "importxt":c.importxt, "savext":c.savext,
            "def": c.def_cmd, "call": c.call
        }
        if k in cmds: cmds[k](v)
        else: raise Exception(f"Unknown command: {k}")

if __name__ == "__main__":
    if os.name == 'nt': os.system('')
    SkipInterpreter().run(sys.argv)
