# Appendix 1
This appendix shows some tricks one can use in Intrepydd

## Automatically return type inference
```python
def func(A: Array(float32, 2), B: Array(float32, 2)) -> Array(bool, 2):
    C = eq(A, B)
    return C
```
can be simplified to
```python
def func(A: Array(float32, 2), B: Array(float32, 2)):
    C = eq(A, B)
    return C
```

## Combined type declaration
```python
def func(A: Array(float32, 2), B: Array(float32, 2)):
    C = eq(A, B)
    return C
```
can be simplified to
```python
def func(A, B: Array(float32, 2)): # A and B both have type Array(float32, 2)
    C = eq(A, B)
    return C
```

## Primitive type abbreviation
all primitive types have an abbreviation, which is adopted from type signature from Java
- `int32`
  - `int` or `I`
- `int64`
  - `long` or `J`
- `float32`
  - `float` or `F`
- `float64`
  - `double` or `D`
  
So   

```python
def func(A, B: Array(float32, 2)):
    C = eq(A, B)
    return C
```
can be simplified to
```python
def func(A, B: Array(F, 2)):
    C = eq(A, B)
    return C
```
