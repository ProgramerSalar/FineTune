# makes sure follow this step 

1. clone this repo: 
    ```
    git clone https://github.com/ProgramerSalar/FineTune.git

    ```

2. install the `req.txt` file 
    ```
    cd FineTune
    pip install -r req.txt 
    ```

3. clone the huggingface repo because in this repo have the pretrained vae weight.
    ```
    cd ..
    git clone https://huggingface.co/ProgramerSalar/vae_model_ckpt
    ```
    
    put the `duffusion_pytorch_model.safetensors` file in the `PATH/vae_ckpt` folder

4. run the `script`
    ```
    cd FineTune
    sh scripts/train_causal_video_vae.sh
    ```