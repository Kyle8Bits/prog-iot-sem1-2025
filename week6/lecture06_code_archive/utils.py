# Ref.: B. Slatkin, Effective Python: 125 Specific Ways to Write Better Python, 
# 3rd ed., Addison-Wesley Professional, 2024.

def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode("utf-8")
    else:
        raise TypeError(f"Must supply str or bytes, found: {data}")
