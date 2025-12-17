# makes sure follow this step 

1. clone the huggingface repo because in this repo have the pretrained vae weight.
    ```
    git clone https://huggingface.co/ProgramerSalar/vae_model_ckpt
    ```
    
    put the `duffusion_pytorch_model.safetensors` file in the `PATH/vae_ckpt` folder

2. clone this repo: 
    ```
    git clone https://github.com/ProgramerSalar/FineTune.git
    ```

3. install the `req.txt` file 
    ```
    cd FineTune
    pip install -r req.txt 
    ```



4. run the `script`
    ```
    sh scripts/train_causal_video_vae.sh
    ```


5. make sure mount the drive file to `colab Notebook`
```
    from google.colab import drive
    drive.mount('/content/drive')
```

6. Download the Dataset file 

```
    cd FineTune/Data
    hf download ProgramerSalar/clip_video clip_video_part_2.zip --repo-type dataset --local-dir .
    unzip clip_video_part_2.zip
```
