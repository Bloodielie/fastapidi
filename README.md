# FastAPI DI

*This library to integrate [pyject](https://github.com/Bloodielie/pyject) into [fastapi](https://github.com/tiangolo/fastapi) to use di*

## Install

```bash
pip install fastapidi
```

## Using

```python
from fastapidi import FastAPIDI, get_dependency

class Test:
    def test(self):
        return "123"

app = FastAPIDI()
app.container.add_singleton(Test, Test)

@app.get("/")
async def test(dependency: Test = get_dependency(Test)):
    return dependency.test()
```
