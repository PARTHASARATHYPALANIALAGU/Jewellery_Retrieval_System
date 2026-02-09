import requests
import os

ENDPOINT = "http://localhost:8000"
TEST_IMG = "**your test image path**"

def test_sketch():
    print(f"🎨 Testing Sketch Search with {TEST_IMG}...")
    try:
        with open(TEST_IMG, "rb") as f:
            files = {"file": f}
            res = requests.post(f"{ENDPOINT}/search/sketch", files=files, timeout=6000) # Long timeout
            
        print(f"🎨 Sketch Status: {res.status_code}")
        if res.status_code == 200:
            print(f"🎨 Success! Got {len(res.json())} results")
        else:
            print(f"❌ Failed: {res.text}")
    except Exception as e:
        print(f"❌ Sketch Exception: {e}")

def test_ocr():
    print(f"📝 Testing OCR with {TEST_IMG}...")
    try:
        with open(TEST_IMG, "rb") as f:
            files = {"file": f}
            res = requests.post(f"{ENDPOINT}/ocr/read", files=files, timeout=6000)
            
        print(f"📝 OCR Status: {res.status_code}")
        if res.status_code == 200:
            print(f"📝 Success! Response: {res.json()}")
        else:
            print(f"❌ Failed: {res.text}")
    except Exception as e:
        print(f"❌ OCR Exception: {e}")

if __name__ == "__main__":
    test_sketch()
    print("-" * 20)
    test_ocr()
