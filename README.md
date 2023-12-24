# AesPA-Net: Aesthetic Pattern-Aware Style Transfer Networks
## Usage
#### Set pretrained weights
* Pretrained models for encoder(VGG-19) can be found in the `./baseline_checkpoints`
  -  Pretrained VGG can be downloaded at [vgg_normalised_conv5_1.t7](https://drive.google.com/drive/folders/1HsJNskEMC5HUimq6ixkSZk7W_hgFNp7J?usp=sharing)
- Prepare pretrained models for **AesPA-Net**
  -  Decoder can be downloaded at [dec_model.pth](https://drive.google.com/file/d/1nb7dQwj7RcQpi8_cURvErSwA-BxyZTT5/view?usp=sharing)
  -  Transformer can be downloaded at [transformer_model.pth](https://drive.google.com/file/d/1YII45EfR3mVbyvqQlzvfiYFIoTCgGG_R/view?usp=sharing)

- Move these pretrained weights to each folders:
  - transformer.pth -> `./train_results/<comment>/log/transformer_model.pth`
  - decoder.pth -> `./train_results/<comment>/log/dec_model.pth`

#### Inference (Automatic)
```
bash scripts/test_styleaware_v2.sh
```
or
```
python main.py --type test --batch_size #batch_size --comment <comment> --content_dir <content_dir> --style_dir <style_dir> --num_workers #num_workers
```


## Citation

```
@InProceedings{Hong_2023_ICCV,
    author    = {Hong, Kibeom and Jeon, Seogkyu and Lee, Junsoo and Ahn, Namhyuk and Kim, Kunhee and Lee, Pilhyeon and Kim, Daesik and Uh, Youngjung and Byun, Hyeran},
    title     = {AesPA-Net: Aesthetic Pattern-Aware Style Transfer Networks},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2023},
    pages     = {22758-22767}
}
```

```
@article{Hong2023AesPANetAP,
  title={AesPA-Net: Aesthetic Pattern-Aware Style Transfer Networks},
  author={Kibeom Hong and Seogkyu Jeon and Junsoo Lee and Namhyuk Ahn and Kunhee Kim and Pilhyeon Lee and Daesik Kim and Youngjung Uh and Hyeran Byun},
  journal={ArXiv},
  year={2023},
  volume={abs/2307.09724},
  url={https://api.semanticscholar.org/CorpusID:259982728}
}
```

## Contact
If you have any question or comment, please contact the first author of this paper - Kibeom Hong

[kibeom9212@gmail.com](kibeom9212@gmail.com)
