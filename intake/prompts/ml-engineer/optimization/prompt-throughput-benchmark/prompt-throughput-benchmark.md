# Throughput Benchmark *AI Prompt *

This prompt builds a benchmark harness for training and inference throughput, including warmup, repeated measurements, GPU monitoring, latency percentiles, and regression detection. It is useful for establishing performance baselines and catching slowdowns over time. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a systematic benchmarking harness to measure and optimize training and inference throughput.

1. Training throughput benchmark:
 - Measure samples/second at batch sizes: 8, 16, 32, 64, 128, 256
 - Run 10 warmup steps, then measure over 100 steps
 - Record: batch size, samples/sec, GPU memory used, GPU utilization %
 - Find the optimal batch size (highest samples/sec while staying within GPU memory budget)

2. Inference throughput benchmark:
 - Measure latency (mean, p50, p95, p99) at batch sizes: 1, 2, 4, 8, 16, 32
 - 100 warmup runs, then 1000 measured runs using torch.cuda.synchronize() for accurate GPU timing
 - Plot: latency vs batch size, throughput vs batch size
 - Find the latency-throughput Pareto frontier

3. Comparison matrix:
 - Benchmark the same model in: PyTorch eager, TorchScript, ONNX Runtime, TensorRT
 - For each: p99 latency and throughput at batch_size=1 and batch_size=32

4. Hardware utilization:
 - Use pynvml to monitor GPU utilization and memory bandwidth utilization during benchmarks
 - Flag if GPU utilization < 70% — indicates compute is not the bottleneck

5. Regression testing:
 - Save benchmark results to a JSON file
 - Compare against baseline: flag if throughput drops > 10% between runs

Return: benchmark harness code, results table, and regression detection script. 
```

## When to use this prompt 
Use case 01 
when you need a repeatable throughput or latency benchmark 
Use case 02 
when comparing batch sizes or execution backends systematically 
Use case 03 
when performance regressions should fail automated checks 
Use case 04 
when you want latency-throughput tradeoff plots and saved baselines 

## What the AI should return 

Benchmark harness code, a results table or JSON output, latency and throughput measurements, and a regression detection script. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Optimization.
