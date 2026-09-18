# Knowledge Distillation *AI Prompt *

This prompt implements knowledge distillation so a smaller student model can learn from a larger teacher using soft targets and optional intermediate feature matching. It is useful when you want much of the teacher's accuracy in a cheaper model. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement knowledge distillation to train a smaller student model to match a larger teacher model.

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

Return: distillation training loop, temperature sweep results, student vs teacher benchmark, and comparison to training from scratch. 
```

## When to use this prompt 
Use case 01 
when compressing a strong but slow teacher model into a faster student 
Use case 02 
when training a student from scratch underperforms 
Use case 03 
when you want to test temperature and alpha settings systematically 
Use case 04 
when intermediate feature distillation may improve student quality 

## What the AI should return 

A distillation training loop, temperature sweep guidance, and a comparison of teacher, distilled student, and student-from-scratch performance. 

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

Once you have the first result, continue deeper with related prompts in Model Compression.
