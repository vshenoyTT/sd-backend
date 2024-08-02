# Stable Diffusion Web Demo

## Introduction
Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input. These instructions pertain to running Stable Diffusion with a web interface on the TT-Wormhole machine.

## How to Run

> [!NOTE]
>
> If you are using Wormhole, you must set the `WH_ARCH_YAML` environment variable.
>
> ```
> export WH_ARCH_YAML=wormhole_b0_80_arch_eth_dispatch.yaml
> ```

To run the demo, make sure to build the project, activate the environment, and set the appropriate environment variables.
For more information, refer [installation and build guide](https://github.com/tenstorrent/tt-metal/blob/main/INSTALLING.md).

Also, clone the frontend component of the demo from this [GitHub repository](https://github.com/vshenoyTT/sd-frontend), following build directions from the README in the linked repository.

Use `python models/demos/wormhole/stable_diffusion/demo/experimental/demo.py` to run the backend server component of the demo, on your TT device.

Then, use `streamlit run streamlit_app.py` to run the frontend component of the demo, on your device connected to the TT device.