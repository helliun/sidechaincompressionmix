# SideChainCompressionMix

This module provides a SideChainCompression class for applying side-chain compression on a pair of input audio files.

## Requirements
- Numpy
- Scipy
- Pydub

You can install these libraries using pip:

bash
pip install numpy scipy pydub


## Usage

To use the SideChainCompression class, you can import it from the sidechaincompressionmix.py module:

python
from sidechaincompressionmix import SideChainCompression


First, create an instance of the class with the paths to your two audio files:

python
side_chain_instance = SideChainCompression("input_file1.wav", "input_file2.wav")


To apply the side-chain compression on the audio files, call the side_chain_compression method:

python
compressed_audio1 = side_chain_instance.side_chain_compression()


If you want to export the resulting compressed audio, use the export_compressed_audio method:

python
side_chain_instance.export_compressed_audio(compressed_audio1, "output_file.wav")


## Example

Here is a simple example demonstrating how to use the SideChainCompression class:

python
from sidechaincompressionmix import SideChainCompression

# Create an instance of the class
side_chain_instance = SideChainCompression("input_file1.wav", "input_file2.wav")

# Apply side-chain compression
compressed_audio1 = side_chain_instance.side_chain_compression()

# Export the resulting compressed audio
side_chain_instance.export_compressed_audio(compressed_audio1, "output_file.wav")


## Notes

- Make sure your audio files are in a format supported by Pydub (such as WAV, MP3, or OGG).
