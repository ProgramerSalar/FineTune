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



https://colab.research.google.com/drive/17S11wwvQwkpo3mPIUsQcoX00ydvzs_I6#scrollTo=EJprBrIUc5bX
