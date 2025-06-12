# DistAlgo Lamport Mutual Exclusion Algorithm

This repository contains an implementation of Lamport's mutual exclusion algorithm in DistAlgo.

## Prerequisites

- **Python 3.7** (DistAlgo does not support Python 3.8+)
- **DistAlgo package**: Install with `py -3.7 -m pip install pyDistAlgo`

## Quick Start

1. **Install DistAlgo**:
   ```bash
   py -3.7 -m pip install pyDistAlgo
   ```

2. **Run the algorithm**:
   ```bash
   py -3.7 -m da lamport.da 3 2
   ```
   - `3` = number of processes
   - `2` = number of critical section requests per process

## Files

- `lamport.da` - Main DistAlgo implementation
- `test.da` - Simple test file to verify DistAlgo installation

## Common Issues & Solutions

### ⚠️ **CRITICAL: Use .da file extension, not .py!**

DistAlgo is a domain-specific language that compiles to Python. Files must have `.da` extension for proper compilation.

### Python Version Issues
- **Error**: `Python version X.Y.Z is not supported`
- **Solution**: Always use `py -3.7` explicitly

### Import Errors
- **Error**: `NameError: name 'process' is not defined`
- **Cause**: Using `.py` extension or wrong Python version
- **Solution**: Use `.da` extension and Python 3.7

### Pattern Matching Errors
- **Error**: `NameError: name 'c2' is not defined`
- **Solution**: Use `some(received(('ack', c2, p)))` for proper variable binding

## Our Debugging Journey

### The Problem Chain
1. **Python Version Conflicts** - System defaulted to Python 3.13
2. **Import Hell** - Treated DistAlgo as regular Python library
3. **Low-Level API Struggles** - Tried to instantiate processes manually
4. **Configuration Nightmares** - Couldn't configure `global_init()` properly
5. **File Extension Revelation** - Used `.py` instead of `.da`
6. **Syntax Issues** - Incorrect pattern matching syntax

### Key Insights
- DistAlgo is a **DSL that compiles to Python**, not a Python library
- **File extensions matter**: `.da` triggers compilation, `.py` runs raw Python
- **Version consistency**: Every command needs explicit `py -3.7`
- **High-level syntax**: Use `process`, `new()`, `start()` after compilation

### Time Investment
~2 hours of debugging to learn: *Sometimes the solution isn't fixing the code—it's using the right tools in the right way.*

## Algorithm Details

This implements a simplified version of Lamport's mutual exclusion algorithm:

1. **Request**: Process sends request with logical timestamp to all others
2. **Acknowledge**: Other processes send acknowledgments
3. **Enter**: Process enters critical section after receiving all acks
4. **Release**: Process sends release message and exits critical section

## Usage Examples

```bash
# 2 processes, 1 request each
py -3.7 -m da lamport.da 2 1

# 5 processes, 3 requests each  
py -3.7 -m da lamport.da 5 3

# Default: 3 processes, 2 requests each
py -3.7 -m da lamport.da
```

## Troubleshooting

If you encounter issues:

1. **Verify Python version**: `py -3.7 --version`
2. **Check DistAlgo installation**: `py -3.7 -c "import da; print(da.__version__)"`
3. **Test with simple file**: `py -3.7 -m da test.da`
4. **Ensure .da extension**: DistAlgo won't work with `.py` files

## References

- [Lamport, L. (1978). "Time, clocks, and the ordering of events in a distributed system"](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
- [DistAlgo Documentation](https://github.com/DistAlgo/distalgo)