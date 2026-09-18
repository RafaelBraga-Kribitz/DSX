# Model Compression *AI Prompts *

7 ML Engineer prompts in Model Compression. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts · 1 chain. 

## AI prompts in Model Compression 
7 prompts Advanced Chain 01 
### Compression Pipeline Chain 

This chain walks through a full compression pipeline: baseline measurement, structured pruning, quantization, optional distillation recovery, deployment export, and Pareto analysis. It is meant for selecting a production-ready compressed model based on measured tradeoffs rather than guesswork. 
Prompt text Step 1: Establish the baseline — measure the uncompressed model: size (MB), FLOPs, p50/p95/p99 inference latency at batch_size=1 and batch_size=32, and accuracy on the full validation set.
Step 2: Pruning — apply structured pruning at 30%, 50%, and 70% sparsity. Fine-tune after each level. Record accuracy, size, and latency at each sparsity level.
Step 3: Quantization — apply INT8 post-training quantization to the pruned model. If accuracy drops > 1%, apply QAT. Record accuracy, size, and latency.
Step 4: Distillation (optional) — if the compressed model still underperforms targets, use the original uncompressed model as a teacher to recover accuracy via knowledge distillation.
Step 5: ONNX export and TensorRT optimization — export the compressed model to TensorRT FP16. Verify numerical correctness. Record final latency and throughput.
Step 6: Accuracy vs efficiency Pareto analysis — plot all tested configurations on an accuracy vs latency scatter plot. Identify the Pareto-optimal point that meets the deployment requirements.
Step 7: Write a compression report: original vs final model comparison (size, latency, FLOPs, accuracy), techniques applied, any accuracy recovery steps taken, and recommendation for production deployment. Copy prompt Open prompt details Intermediate Single prompt 02 
### Knowledge Distillation 

This prompt implements knowledge distillation so a smaller student model can learn from a larger teacher using soft targets and optional intermediate feature matching. It is useful when you want much of the teacher's accuracy in a cheaper model. 
Prompt text Implement knowledge distillation to train a smaller student model to match a larger teacher model.

Teacher model: {{teacher_model}} (large, high-accuracy, slow)
Student model: {{student_model}} (small, faster, to be trained)

1. Soft target distillation (Hinton et al. 2015):
 - Get teacher soft probabilities: softmax(teacher_logits / temperature)
 - Student loss = α × KL_divergence(student_soft, teacher_soft) + (1-α) × CrossEntropy(student, hard_labels)
 - Temperature T: higher T produces softer distributions (try T=3, T=5, T=10)
 - α: weight between distillation loss and task loss (try α=0.7)

2. Intermediate layer distillation (better for deep networks):
 - Match intermediate feature maps between teacher and student layers
 - Use an adapter layer if teacher and student have different hidden dimensions
 - Feature distillation loss: MSE(student_features, teacher_features)

3. Training procedure:
 - Freeze teacher model (no gradients)
 - Train student with combined loss
 - Use a slightly higher learning rate than training from scratch
 - Run for same number of epochs as training student from scratch

4. Evaluation:
 - Student accuracy vs teacher accuracy
 - Student accuracy vs same architecture trained from scratch (distillation should outperform)
 - Student inference latency vs teacher inference latency

5. Self-distillation variant:
 - If no pre-trained teacher exists: use the model's own earlier epochs as the teacher

Return: distillation training loop, temperature sweep results, student vs teacher benchmark, and comparison to training from scratch. Copy prompt Open prompt details Intermediate Single prompt 03 
### ONNX Export and Validation 

This prompt exports a PyTorch model to ONNX, validates graph correctness, compares outputs against PyTorch, and benchmarks ONNX Runtime performance. It is useful when preparing a model for portable or faster inference beyond eager PyTorch. 
Prompt text Export this PyTorch model to ONNX format and validate correctness and performance.

1. Export to ONNX:
 - Use torch.onnx.export with opset_version=17 (latest stable)
 - Define input_names, output_names, and dynamic_axes for variable batch size and sequence length
 - Set do_constant_folding=True for graph optimization
 - Use dynamo=True (torch.onnx.dynamo_export) for newer models with control flow

2. ONNX graph validation:
 - onnx.checker.check_model(model) for structural validity
 - onnxsim (onnx-simplifier): simplify the graph and remove redundant nodes
 - Visualize with Netron to inspect the computation graph

3. Numerical correctness check:
 - Run inference with identical inputs through PyTorch and ONNX Runtime
 - Assert all outputs match to within rtol=1e-3, atol=1e-5
 - Test with multiple batch sizes and sequence lengths if dynamic axes are used

4. ONNX Runtime inference:
 - Create InferenceSession with providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
 - Optimize with ort.SessionOptions: graph_optimization_level=ORT_ENABLE_ALL
 - Enable io_binding for zero-copy GPU inference

5. Performance benchmark:
 - Compare p50/p95/p99 latency: PyTorch vs ONNX Runtime
 - Compare throughput at batch sizes 1, 8, 32
 - Typical improvement: 1.5–4× speedup on CPU, 1.2–2× on GPU

6. Common export issues and fixes:
 - Control flow (if/else in forward): use torch.jit.script first
 - Custom ops: register custom ONNX op or rewrite using supported ops
 - Dynamic shapes: test with min, typical, and max shapes

Return: export script, validation code, numerical correctness tests, and benchmark results. Copy prompt Open prompt details Beginner Single prompt 04 
### Post-Training Quantization 

This prompt applies post-training quantization and, if needed, quantization-aware training to reduce model size and improve inference speed. It includes validation steps so compression gains can be weighed against accuracy loss. 
Prompt text Apply post-training quantization (PTQ) to reduce model size and inference latency.

1. INT8 static quantization (PyTorch):
 - Prepare model: torch.quantization.prepare with a QConfig
 - Calibrate on a representative dataset (100–1000 samples): run forward passes to collect activation statistics
 - Convert: torch.quantization.convert to replace float ops with int8 ops
 - Save and measure: model size before vs after, inference latency before vs after

2. INT8 dynamic quantization:
 - torch.quantization.quantize_dynamic for models where activation ranges vary greatly
 - Suitable for: LSTMs, linear layers in NLP models
 - No calibration step needed

3. Quantization-aware training (QAT) if accuracy drops > 1%:
 - Insert fake quantization nodes during training
 - Fine-tune for {{qat_epochs}} epochs at a lower learning rate
 - Convert to fully quantized model after training

4. Accuracy validation:
 - Evaluate quantized model on the full validation set
 - Acceptable accuracy drop: < 1% for most production use cases
 - If accuracy drops significantly: try QAT, or quantize only the later layers

5. ONNX + ONNX Runtime INT8:
 - Export to ONNX, then apply ONNXRuntime quantization
 - ort.quantization.quantize_dynamic or quantize_static
 - Often faster than PyTorch native quantization on CPU

Return: PTQ implementation, QAT setup, accuracy comparison table, and latency/size improvement metrics. Copy prompt Open prompt details Intermediate Single prompt 05 
### Structured Pruning 

This prompt performs structured pruning that removes whole filters, channels, or heads so real hardware speedups are possible. It includes sensitivity analysis, iterative prune-and-fine-tune cycles, and measurement of actual latency and accuracy tradeoffs. 
Prompt text Apply structured pruning to reduce this model's size and inference cost.

Unstructured pruning (individual weight zeroing) does not improve real-world latency without sparse hardware. Structured pruning removes entire filters, channels, or layers for actual speedup.

1. Sensitivity analysis:
 - For each layer, measure accuracy impact of removing that layer entirely
 - Rank layers from least to most sensitive
 - Layers early in the network and the last classification layer are typically most sensitive

2. Filter/channel pruning (for CNNs):
 - Score filters by L1-norm of weights (smaller norm = less important)
 - Remove the bottom {{prune_ratio}}% of filters in each prunable layer
 - Handle channel dimension changes: update the next layer's input channels accordingly
 - Re-run BN calibration after pruning

3. Attention head pruning (for transformers):
 - Score attention heads by mean attention entropy or gradient-based importance
 - Remove the {{num_heads_to_prune}} least important heads per layer
 - Adjust head projection dimensions accordingly

4. Iterative pruning and fine-tuning:
 - Prune → fine-tune → prune → fine-tune (gradual pruning is better than one-shot)
 - Use a cosine pruning schedule that increases sparsity gradually
 - Target sparsity: {{target_sparsity}}%

5. Results measurement:
 - FLOPs reduction
 - Parameter reduction
 - Inference latency reduction (must measure on real hardware, not estimate)
 - Accuracy change vs unpruned model

Return: sensitivity analysis, pruning implementation, fine-tuning loop, and results table. Copy prompt Open prompt details Advanced Single prompt 06 
### TensorRT Optimization 

This prompt optimizes NVIDIA GPU inference with TensorRT through an ONNX-based pipeline, optional FP16 or INT8 precision, calibration, and engine serialization. It is meant for teams chasing the lowest possible latency on supported NVIDIA hardware. 
Prompt text Optimize this model for NVIDIA GPU inference using TensorRT.

1. Conversion path: PyTorch → ONNX → TensorRT engine
 - Export to ONNX (opset 17, dynamic axes for batch)
 - Build TensorRT engine using trtexec or the TensorRT Python API

2. Precision selection:
 - FP32: baseline, no accuracy loss
 - FP16: enable with builder_config.set_flag(trt.BuilderFlag.FP16) — typically 2× speedup, minimal accuracy loss
 - INT8: requires calibration dataset for activation range statistics. Use IInt8EntropyCalibrator2. Up to 4× speedup, requires validation.

3. Engine build configuration:
 - Set optimization profiles for dynamic shape engines: min, optimal, and max input shapes
 - workspace size: 4GB (larger allows TensorRT to try more kernel alternatives)
 - Enable timing cache for faster re-builds

4. INT8 calibration:
 - Provide 100–500 representative calibration samples (not validation set)
 - Run calibration and save calibration table for reuse
 - Validate accuracy: if accuracy drops > 1%, use layer-wise precision override for sensitive layers

5. Layer-wise precision override:
 - Keep the first and last layers in FP32
 - Mark softmax and normalization layers as FP32
 - Use FP16 or INT8 for the bulk of the network

6. Performance measurement:
 - Use trtexec --percentile=99 for accurate p99 latency
 - Compare: PyTorch eager, TorchScript, ONNX Runtime, TensorRT FP16, TensorRT INT8

7. Engine serialization and loading:
 - Serialize engine to disk — engines are GPU-specific, not portable
 - Load at inference time and bind input/output buffers

Return: full TensorRT conversion pipeline, INT8 calibration code, precision comparison table, and engine serving wrapper. Copy prompt Open prompt details Advanced Single prompt 07 
### Weight Sharing and Low-Rank Decomposition 

This prompt compresses large weight matrices using low-rank decomposition or LoRA-style adaptations, with rank sweeps and mixed-rank strategies guided by sensitivity. It is useful when large linear layers dominate parameter count and compute cost. 
Prompt text Apply low-rank matrix decomposition to compress the large weight matrices in this model.

1. Identify compression targets:
 - Profile all weight matrices by parameter count and FLOPs contribution
 - Focus on large linear layers (embedding, feed-forward, projection layers)
 - Attention QKV matrices and output projections in transformers are primary targets

2. SVD-based decomposition:
 - For weight matrix W (m × n), compute SVD: W = U × S × Vt
 - Keep only top-k singular values: W ≈ U_k × S_k × Vt_k
 - Rank k selection: sweep k values and measure accuracy vs compression tradeoff
 - Replace original layer with two consecutive smaller layers: Linear(in, k) + Linear(k, out)
 - Break-even rank: k < (m × n) / (m + n) reduces parameter count

3. LoRA (Low-Rank Adaptation) for fine-tuning:
 - Freeze base model weights
 - Add trainable low-rank matrices A (d × r) and B (r × k) in parallel with frozen weights
 - Output = Wx + BAx × (alpha/r)
 - Typical ranks: r=4, r=8, r=16, r=64
 - Merge LoRA weights back into base model for inference: W_new = W + B × A

4. Accuracy evaluation:
 - Measure accuracy at compression ratios: 25%, 50%, 75% parameter reduction
 - Plot accuracy vs compression ratio curve
 - Find the Pareto-optimal point

5. Mixed-rank strategy:
 - Apply higher compression to less sensitive layers, lower compression to sensitive ones
 - Use gradient-based layer sensitivity to guide rank assignment

Return: SVD decomposition code, LoRA implementation, compression curve, and mixed-rank strategy. Copy prompt Open prompt details 
## Recommended Model Compression workflow 
1 
### Compression Pipeline Chain 

Start with a focused prompt in Model Compression so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Knowledge Distillation 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### ONNX Export and Validation 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Post-Training Quantization 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
