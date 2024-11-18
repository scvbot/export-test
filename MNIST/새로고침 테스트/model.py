"\"import torch\\nimport torch.nn as nn\\n\\n# 모델 이름: model_10_v14\\n# 데이터셋: MNIST\\n# 학습 데이터 수: 50000\\n# 테스트 데이터 수: 10000\\n# 레이블 수: 10\\n# 에폭 수: 2\\n\\nclass Model(nn.Module):\\n    def __init__(self):\\n        super().__init__()\\n\\n        self.layer0 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=(10, 10), stride=(1, 1), padding=(0, 0), dilation=(1, 1), groups=1, padding_mode='zeros', bias=True)\\n        self.layer1 = nn.Flatten(start_dim=1, end_dim=-1)\\n        self.layer2 = nn.Linear(in_features=3610, out_features=10, bias=True)\\n\\n    def forward(self, x):\\n        # Input shape: [batch_size, channels, height, width]\\n        x = self.layer0(x)\\n        x = self.layer1(x)\\n        x = self.layer2(x)\\n        return x\\n\\nif __name__ == '__main__':\\n    # 모델 인스턴스 생성\\n    model = Model()\\n    print('모델 구조:')\\n    print(model)\\n    \\n    # 입력 텐서 예제\\n    batch_size = 1  # 배치 크기\\n    channels = 1  # 입력 채널 수\\n    height = 28  # 입력 높이\\n    width = 28  # 입력 너비\\n    x = torch.randn(batch_size, channels, height, width)\\n    \\n    # 순전파 실행\\n    output = model(x)\\n    print(f'입력 shape: {x.shape}')\\n    print(f'출력 shape: {output.shape}')\""