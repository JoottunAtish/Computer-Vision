You got it\! Here is the improved README in clear Markdown format, ready to be copied into your project:

-----

# 👁️ Computer Vision Assignments

A repository containing selected laboratory assignments focused on **fundamental computer vision techniques** implemented using Python.

-----

## 📘 Selected Laboratory Assignments

These labs cover essential topics in image processing and feature detection:

  * **Lab 4: Sobel Transformation**
      * Focus: Implementing the **Sobel operator** for robust **edge detection**.
  * **Lab 5: Canny Edge Detection**
      * Focus: Implementing the **Canny algorithm**, a multi-stage approach for optimal edge detection.
  * **Lab 6: Hough Transformation**
      * Focus: Utilizing the **Hough Transform** for detecting **lines and circles** in images.
  * **Lab 7: Harris Corner Detection**
      * Focus: Implementing the **Harris algorithm** to identify distinctive **corners** (interest points) in an image.

-----

## 🛠️ Installation and Setup

This project uses **UV**, a fast Python package installer and resolver, for dependency management.

### Prerequisites

You must have the **UV project manager** installed on your system.

### 1\. Setup UV (Windows)

Run the following command in your PowerShell to install the UV installer:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> **Note:** For non-Windows environments (Linux/macOS), please refer to the official [UV documentation](https://astral.sh/uv) for the appropriate installation command.

### 2\. Install Dependencies

Once UV is set up, navigate to the project root directory and run the following command. This will create a virtual environment and install all required packages:

```bash
uv sync
```

-----

## ▶️ Usage

To run a specific lab script (e.g., `lab_4_sobel.py`), first ensure your virtual environment is active, and then execute the file using Python.
