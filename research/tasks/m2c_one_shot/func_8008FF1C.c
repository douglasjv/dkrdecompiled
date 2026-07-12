#include "../../../ctx.c"
void func_8008FF1C(s32 arg0) {
    s32 sp7C;
    s32 sp6C;
    s32 sp60;
    s32 *sp5C;
    Settings *sp58;
    DrawTexture *var_v0;
    Gfx *temp_v1;
    TrackRenderDetails *var_s0;
    TrackRenderDetails *var_s0_2;
    s32 temp_s2;
    s32 temp_t3;
    s32 var_s3;
    s32 var_s6;
    s8 *temp_s1;
    u8 temp_t0;
    u8 temp_t1;
    u8 temp_t3_2;
    u8 temp_t5;
    u8 temp_t6;
    u8 temp_t7;
    u8 temp_v0;

    sp58 = get_settings();
    sp5C = get_misc_asset(0x1A);
    if ((gMenuDelay >= -0x16) && (gMenuDelay < 0x17)) {
        if (gFFLUnlocked == -1) {
            sp60 = 3;
        } else {
            sp60 = 4;
        }
        var_s0 = gTrackSelectRenderDetails;
        sp7C = -1;
        sp6C = (s32) (gTrackSelectX / 320.0f);
        var_s3 = (s32) (gTrackSelectY / (f32) -gTrackSelectViewportY) - 1;
        do {
            var_s6 = -1;
loop_7:
            if ((var_s3 < 0) || (temp_s2 = sp6C + var_s6, ((sp60 < var_s3) != 0)) || (temp_s2 < 0) || (temp_s2 >= 6)) {
                var_s0->visible = 0;
            } else {
                var_s0->visible = 1;
                var_s0->hubName = level_name(level_world_id(var_s3 + 1));
                if (*((var_s3 * 0xC) + (temp_s2 * 2) + gTrackSelectIDs) != -1) {
                    temp_s1 = (var_s3 * 6) + temp_s2 + sp5C;
                    var_s0->trackName = level_name((s32) *temp_s1);
                    if (temp_s2 == 4) {
                        if ((((s32) sp58->trophies >> (var_s3 * 2)) & 3) == 3) {
                            var_s0->visible = 2;
                        }
                    } else if (sp58->courseFlagsPtr[*temp_s1] & 2) {
                        var_s0->visible = 2;
                    }
                } else {
                    var_s0->trackName = gQMarkPtr;
                }
                var_s0->xOff = (s16) (s32) ((f32) (temp_s2 * 0x140) - gTrackSelectX);
                var_s0->opacity = 0xFF;
                var_s0->yOff = (s16) (s32) ((f32) (-var_s3 * gTrackSelectViewportY) - gTrackSelectY);
                if ((temp_s2 == gSelectedTrackX) && (var_s3 == gSelectedTrackY)) {
                    var_s0->copyViewPort |= 0x80;
                    if (gOpacityDecayTimer < 0x20) {
                        var_s0->opacity = gOpacityDecayTimer * 8;
                    }
                } else {
                    var_s0->copyViewPort &= 0xFF7F;
                }
                temp_t7 = var_s0->copyViewPort & 0xFF80;
                var_s0->copyViewPort = temp_t7;
                if (gMenuDelay == 0) {
                    if (var_s3 > 0) {
                        var_s0->copyViewPort = ((temp_t7 | 1) & 0x7F) | (temp_t7 & 0xFF80);
                    }
                    if (temp_s2 < 5) {
                        temp_t3_2 = var_s0->copyViewPort;
                        var_s0->copyViewPort = ((temp_t3_2 | 2) & 0x7F) | (temp_t3_2 & 0xFF80);
                    }
                    if (var_s3 < sp60) {
                        temp_t0 = var_s0->copyViewPort;
                        var_s0->copyViewPort = ((temp_t0 | 4) & 0x7F) | (temp_t0 & 0xFF80);
                    }
                    if (temp_s2 > 0) {
                        temp_t5 = var_s0->copyViewPort;
                        var_s0->copyViewPort = ((temp_t5 | 8) & 0x7F) | (temp_t5 & 0xFF80);
                    }
                    if ((temp_s2 == 4) && (var_s3 == 4)) {
                        temp_t1 = var_s0->copyViewPort;
                        var_s0->copyViewPort = (temp_t1 & 0x7D) | (temp_t1 & 0xFF80);
                    }
                    if ((temp_s2 == 5) && (var_s3 == 3)) {
                        temp_t6 = var_s0->copyViewPort;
                        var_s0->copyViewPort = (temp_t6 & 0x7B) | (temp_t6 & 0xFF80);
                    }
                }
                if (temp_s2 == 4) {
                    var_s0->border = 6;
                } else if (temp_s2 == 5) {
                    var_s0->border = 5;
                } else {
                    var_s0->border = 4;
                }
            }
            var_s6 += 1;
            var_s0 += 0x10;
            if (var_s6 != 2) {
                goto loop_7;
            }
            var_s3 += 1;
            temp_t3 = sp7C + 1;
            sp7C = temp_t3;
        } while (temp_t3 < 2);
        camDisableUserView(0, 1);
        menu_camera_centre();
        mtx_ortho(&sMenuCurrDisplayList, &sMenuCurrHudMat);
        rendermode_reset(&sMenuCurrDisplayList);
        temp_v1 = sMenuCurrDisplayList;
        sMenuCurrDisplayList = temp_v1 + 8;
        temp_v1->words.w1 = 0;
        temp_v1->words.w0 = 0xE7000000;
        D_80126928 = 0x40;
        D_8012692C = 0x20;
        gTrackMenuHubName = NULL;
        var_s0_2 = gTrackSelectRenderDetails;
        sp7C = 0;
        do {
            temp_v0 = var_s0_2->visible;
            if (temp_v0 != 0) {
                var_v0 = D_800E05F4;
                if (temp_v0 == 1) {
                    var_v0 = D_800E05D4;
                }
                trackmenu_render_2D((s32) var_s0_2->xOff, (s32) var_s0_2->yOff, var_s0_2->hubName, var_s0_2->trackName, (s32) var_s0_2->opacity, (s32) var_s0_2->border, (s32) ((u16) var_s0_2->viewPort >> 0xF), var_v0, var_s0_2->copyViewPort & 0x7F);
            }
            var_s0_2 += 0x10;
        } while (var_s0_2 != gPlayerSelectVehicle);
        gTrackSelectVertsFlip = 1 - gTrackSelectVertsFlip;
    }
}
