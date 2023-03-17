#requirements: numpy, scipy, pydub

# imports
from sidechaincompressionmix import SideChainCompression

# code
def main():
    # Define audio file paths
    file1 = "path/to/your/audio1.wav"
    file2 = "path/to/your/audio2.wav"
    output_file_path = "path/to/your/compressed_audio_output.wav"

    # Create the SideChainCompression object
    side_chain_compression = SideChainCompression(file1, file2)

    # Apply side-chain compression
    compressed_audio = side_chain_compression.side_chain_compression()

    # Export the compressed audio
    side_chain_compression.export_compressed_audio(compressed_audio, output_file_path)

    print("Compressed audio has been exported successfully.")

if __name__ == "__main__":
    main()