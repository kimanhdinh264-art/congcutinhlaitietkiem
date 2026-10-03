import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm-Đinh Thị Kim Anh",
    page_icon="💰",
    layout="centered"
)

# ==============================
# TIÊU ĐỀ
# ==============================
st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

st.divider()

# ==============================
# NHẬP THÔNG TIN
# ==============================

so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=100_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# ==============================
# HÀM ĐỊNH DẠNG TIỀN
# ==============================

def dinh_dang_tien(so_tien):
    return f"{so_tien:,.0f} VNĐ".replace(",", ".")


# ==============================
# TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Chuyển lãi suất từ % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Kỳ hạn tính theo năm
    so_nam = ky_han / 12

    # Tổng tiền lãi
    tong_tien_lai = so_tien_gui * lai_suat_nam * so_nam

    # ==============================
    # TÍNH LÃI THEO HÌNH THỨC NHẬN
    # ==============================

    if hinh_thuc == "Cuối kỳ":

        so_ky_nhan_lai = 1

        lai_dinh_ky = tong_tien_lai

        mo_ta_ky = "Tổng tiền lãi nhận vào cuối kỳ"

    elif hinh_thuc == "Hàng tháng":

        so_ky_nhan_lai = ky_han

        lai_dinh_ky = tong_tien_lai / so_ky_nhan_lai

        mo_ta_ky = "Tiền lãi nhận mỗi tháng"

    else:  # Hàng quý

        so_ky_nhan_lai = ky_han / 3

        lai_dinh_ky = tong_tien_lai / so_ky_nhan_lai

        mo_ta_ky = "Tiền lãi nhận mỗi quý"

    # Tổng gốc + lãi
    tong_tien_nhan = so_tien_gui + tong_tien_lai

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================

    st.success("✅ Tính toán thành công!")

    st.subheader("📊 KẾT QUẢ")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💵 Tiền gửi",
            dinh_dang_tien(so_tien_gui)
        )

    with col2:
        st.metric(
            "📈 Lãi suất",
            f"{lai_suat:.2f}%/năm"
        )

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "📅 Kỳ hạn",
            f"{ky_han} tháng"
        )

    with col4:
        st.metric(
            "💳 Nhận lãi",
            hinh_thuc
        )

    st.divider()

    # Tiền lãi định kỳ
    st.info(
        f"💰 **{mo_ta_ky}: {dinh_dang_tien(lai_dinh_ky)}**"
    )

    # Tổng tiền lãi
    st.warning(
        f"📈 **Tổng tiền lãi: {dinh_dang_tien(tong_tien_lai)}**"
    )

    # Tổng gốc + lãi
    st.success(
        f"🏦 **Tổng tiền gốc + tiền lãi: {dinh_dang_tien(tong_tien_nhan)}**"
    )

    # ==============================
    # BẢNG TÓM TẮT
    # ==============================

    st.divider()

    st.subheader("📋 Bảng tóm tắt")

    ket_qua = {
        "Thông tin": [
            "Số tiền gửi",
            "Kỳ hạn",
            "Lãi suất",
            "Hình thức nhận lãi",
            "Tiền lãi định kỳ",
            "Tổng tiền lãi",
            "Tổng gốc + lãi"
        ],
        "Kết quả": [
            dinh_dang_tien(so_tien_gui),
            f"{ky_han} tháng",
            f"{lai_suat:.2f}%/năm",
            hinh_thuc,
            dinh_dang_tien(lai_dinh_ky),
            dinh_dang_tien(tong_tien_lai),
            dinh_dang_tien(tong_tien_nhan)
        ]
    }

    st.table(ket_qua)

# ==============================
# GHI CHÚ
# ==============================

st.divider()

st.caption(
    "Lưu ý: Kết quả được tính theo phương pháp lãi đơn, "
    "chưa xét đến các chính sách thực tế của từng ngân hàng."
)
