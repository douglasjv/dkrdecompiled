#include "../../../ctx.c"
static ? D_800E64D0;                                /* unable to generate initializer: unknown type; const */
static ? D_800E6538;                                /* unable to generate initializer: unknown type; const */

void func_80049794(s32 arg0, f32 arg1, Object *arg2, Object_Racer *arg3) {
    f32 spEC;
    f32 spE8;
    f32 spE4;
    f32 spE0;
    f32 spDC;
    f32 spD8;
    f32 spD4;
    f32 spD0;
    f32 spC8;
    f32 spC4;
    s32 spB8;
    s8 spA3;
    s8 spA2;
    s8 spA1;
    s8 sp5F;
    f64 sp48;
    AttachPoint *temp_v1_17;
    AttachPoint *temp_v1_18;
    Object *temp_v0_14;
    Object *temp_v0_15;
    Object *temp_v0_16;
    Object *temp_v0_17;
    Object *temp_v0_18;
    Object_Racer *var_v1_3;
    WaterProperties **var_v0;
    WaterProperties **var_v0_2;
    f32 *temp_v1_2;
    f32 temp_f0;
    f32 temp_f0_11;
    f32 temp_f0_12;
    f32 temp_f0_13;
    f32 temp_f0_14;
    f32 temp_f0_15;
    f32 temp_f0_2;
    f32 temp_f0_3;
    f32 temp_f0_5;
    f32 temp_f0_6;
    f32 temp_f0_7;
    f32 temp_f12;
    f32 temp_f14;
    f32 temp_f14_2;
    f32 temp_f20;
    f32 temp_f20_2;
    f32 temp_f2;
    f32 temp_f2_2;
    f32 temp_f2_3;
    f32 temp_f2_4;
    f32 temp_f2_5;
    f32 temp_f2_6;
    f32 var_f0;
    f32 var_f0_2;
    f32 var_f0_5;
    f32 var_f12;
    f32 var_f12_2;
    f32 var_f12_3;
    f32 var_f12_4;
    f32 var_f14;
    f32 var_f14_2;
    f32 var_f14_3;
    f32 var_f20;
    f32 var_f20_2;
    f32 var_f20_3;
    f32 var_f20_4;
    f32 var_f20_5;
    f32 var_f20_6;
    f32 var_f20_7;
    f32 var_f20_8;
    f32 var_f2;
    f32 var_f2_2;
    f32 var_f8;
    f64 temp_f0_10;
    f64 temp_f0_4;
    f64 temp_f0_8;
    f64 temp_f0_9;
    f64 var_f0_3;
    f64 var_f0_4;
    f64 var_f0_6;
    s16 temp_a0;
    s16 temp_v0_12;
    s16 temp_v1_10;
    s16 temp_v1_11;
    s16 temp_v1_12;
    s16 temp_v1_13;
    s16 temp_v1_15;
    s16 temp_v1_16;
    s16 temp_v1_3;
    s16 temp_v1_4;
    s16 temp_v1_5;
    s16 temp_v1_6;
    s16 temp_v1_7;
    s16 temp_v1_8;
    s16 temp_v1_9;
    s16 var_t4_2;
    s32 temp_a0_3;
    s32 temp_f10;
    s32 temp_f18;
    s32 temp_f4;
    s32 temp_f6;
    s32 temp_t0_2;
    s32 temp_t5;
    s32 temp_t6;
    s32 temp_t7;
    s32 temp_t9;
    s32 temp_v0_2;
    s32 temp_v0_3;
    s32 temp_v1;
    s32 var_a0;
    s32 var_a0_2;
    s32 var_a1;
    s32 var_a1_2;
    s32 var_at;
    s32 var_at_2;
    s32 var_at_3;
    s32 var_at_4;
    s32 var_t0;
    s32 var_t0_2;
    s32 var_t0_3;
    s32 var_t0_4;
    s32 var_t0_5;
    s32 var_v0_3;
    s32 var_v0_4;
    s32 var_v0_5;
    s32 var_v0_6;
    s32 var_v1;
    s32 var_v1_2;
    s8 temp_a0_2;
    s8 temp_a1;
    s8 temp_a3;
    s8 temp_t0;
    s8 temp_v0;
    s8 temp_v0_10;
    s8 temp_v0_11;
    s8 temp_v0_13;
    s8 temp_v0_4;
    s8 temp_v0_6;
    s8 temp_v0_7;
    s8 temp_v0_8;
    s8 temp_v1_14;
    s8 var_t2;
    s8 var_t4;
    s8 var_t8;
    u32 temp_v0_9;
    u8 temp_v0_19;
    u8 temp_v0_5;
    void *temp_v1_19;

    if (func_8000E138() != 0) {
        arg1 = (f32) ((f64) arg1 * 1.09);
    }
    sp5F = 0;
    if (arg3->groundedWheels > 0) {
        arg3->unk84 = 0.0f;
        arg3->unk88 = 0.0f;
    }
    if ((arg3->unk1FE == 4) && (arg3->spinout_timer == 0)) {
        sound_play(0x240U, NULL);
        arg3->spinout_timer = 0x14;
    }
    var_t2 = 0;
    if ((gCurrentPlayerIndex != -1) && (arg3->vehicleIDPrev != 0xC) && (temp_v1 = gRacerWaveCount - 1, (gRacerWaveCount != 0))) {
        var_a0 = temp_v1;
        if (temp_v1 >= 0) {
            var_v0 = &gRacerCurrentWave[var_a0];
            temp_f0 = arg2->trans.position.f[1] + 5.0f;
            if ((*var_v0)->waveHeight < temp_f0) {
loop_12:
                var_a0 -= 1;
                var_v0 -= 4;
                if (var_a0 >= 0) {
                    if ((*var_v0)->waveHeight < temp_f0) {
                        goto loop_12;
                    }
                }
            }
        }
        var_a1 = var_a0 * 4;
        var_v0_2 = &gRacerCurrentWave[var_a0];
        if (var_a0 == temp_v1) {
            var_a1 -= 4;
            var_v0_2 -= 4;
        }
        temp_f2 = (arg2->trans.position.f[1] - *var_v0_2->unk4) - 10.0f;
        if (temp_f2 > 100.0f) {
            arg3->drift_direction = 0;
        }
        var_f0 = -arg3->velocity;
        if (var_f0 < 0.0f) {
            var_f0 = 0.0f;
        }
        if ((temp_f2 < 35.0f) && ((f64) var_f0 < 8.0)) {
            var_t2 = 1;
        }
        if ((arg3->drift_direction == 0) && (temp_f2 < 38.0f) && ((f64) var_f0 >= 8.0)) {
            arg3->drift_direction = 1;
        }
        temp_v0 = arg3->trickType;
        if ((temp_v0 == 1) || (temp_v0 == -1) || ((f64) (gRacerCurrentWave + var_a1)->unk4->unk8 < 0.3999999164137989)) {
            arg3->drift_direction = 0;
            var_t2 = 0;
        }
        if (arg3->drift_direction != 0) {
            if (((f64) var_f0 < 8.0) || (gCurrentStickY < -0xA)) {
                arg3->drift_direction = 0;
            }
            var_f0_2 = var_f0 - 8.0f;
            if ((f64) var_f0_2 > 4.0) {
                var_f0_2 = 4.0f;
            }
            arg2->trans.position.f[1] += ((38.0f - temp_f2) * arg1 * (var_f0_2 / 4.0f)) / 8.0f;
            if (gCurrentStickY > 0) {
                gCurrentStickY = (s32) gCurrentStickY >> 1;
            }
        }
    }
    D_8011D550 = 0;
    gCurrentCarSteerVel = 0;
    D_8011D558 = 0;
    spE8 = arg2->trans.position.f[0];
    spE4 = arg2->trans.position.f[1];
    spE0 = arg2->trans.position.f[2];
    if (arg3->trickType != 0) {
        var_f2 = 4.0f;
    } else {
        var_f2 = 8.0f;
    }
    temp_a1 = arg3->steerAngle;
    temp_v0_2 = gCurrentStickX - temp_a1;
    temp_f10 = (s32) (((f32) temp_v0_2 * arg1) / var_f2);
    var_v1 = temp_f10;
    if (temp_v0_2 != 0) {
        var_t8 = temp_a1 + var_v1;
        if (temp_f10 == 0) {
            if (temp_v0_2 > 0) {
                var_v1 = 1;
            }
            var_t8 = temp_a1 + var_v1;
            if (temp_v0_2 < 0) {
                var_v1 = -1;
                goto block_49;
            }
        }
    } else {
block_49:
        var_t8 = temp_a1 + var_v1;
    }
    arg3->steerAngle = var_t8;
    temp_a3 = arg3->unk1E8;
    temp_v0_3 = gCurrentStickY - temp_a3;
    temp_f6 = (s32) ((f64) ((f32) temp_v0_3 * arg1) * 0.0625);
    var_v1_2 = temp_f6;
    if (temp_v0_3 != 0) {
        var_t4 = temp_a3 + var_v1_2;
        if (temp_f6 == 0) {
            if (temp_v0_3 > 0) {
                var_v1_2 = 1;
            }
            var_t4 = temp_a3 + var_v1_2;
            if (temp_v0_3 < 0) {
                var_v1_2 = -1;
                goto block_56;
            }
        }
    } else {
block_56:
        var_t4 = temp_a3 + var_v1_2;
    }
    arg3->unk1E8 = var_t4;
    spA2 = var_t2;
    handle_racer_items(arg2, arg3, arg0);
    func_800535C4(arg2, arg3);
    racer_attack_handler_plane(arg2, arg3);
    if (gCurrentPlayerIndex != -1) {
        handle_racer_head_turning(arg2, arg3, arg0);
    } else {
        slowly_reset_head_angle(arg3);
    }
    if (gCurrentRacerInput & 0x8000) {
        var_f0_3 = (f64) arg1;
        arg3->throttle = (f32) ((f64) arg3->throttle + (var_f0_3 * 0.01));
        if ((f64) arg3->throttle > 1.0) {
            var_f8 = 1.0f;
            goto block_65;
        }
    } else {
        var_f0_3 = (f64) arg1;
        arg3->throttle = (f32) ((f64) arg3->throttle - (var_f0_3 * 0.01));
        if (arg3->throttle < 0.0f) {
            var_f8 = 0.0f;
block_65:
            arg3->throttle = var_f8;
        }
    }
    if (arg3->exitObj != NULL) {
        arg3->throttle = 0.5f;
    }
    spC8 = arg3->throttle;
    if ((gCurrentRacerInput & 0x4000) && ((gCurrentStickY < -0x28) || (arg3->velocity < 0.0f))) {
        arg3->brake = (f32) ((f64) arg3->brake + (var_f0_3 * 0.016));
        if (*(&D_800E64D0 + 4) < (f64) arg3->brake) {
            arg3->brake = 1.2f;
        }
        if (((f64) arg3->velocity < -2.0) && (arg3->groundedWheels >= 2)) {
            rumble_set(arg3->playerIndex, 3U);
        }
    } else {
        arg3->brake = (f32) ((f64) arg3->brake - (var_f0_3 * 0.016));
        if (arg3->brake < 0.0f) {
            arg3->brake = 0.0f;
        }
    }
    spC4 = arg3->brake;
    gCurrentRacerTransform.rotation.s[0] = arg2->trans.rotation.s[0];
    gCurrentRacerTransform.rotation.s[2] = 0;
    gCurrentRacerTransform.position.f[0] = 0.0f;
    gCurrentRacerTransform.position.f[1] = 0.0f;
    gCurrentRacerTransform.position.f[2] = 0.0f;
    gCurrentRacerTransform.rotation.s[1] = arg2->trans.rotation.s[1];
    gCurrentRacerTransform.scale = 1.0f;
    mtxf_from_transform((f32 (*)[4][4]) &sp60[0][0], &gCurrentRacerTransform);
    mtxf_transform_point(M2C_ERROR(/* Read from unset register $f12 */), M2C_ERROR(/* Read from unset register $f14 */), 0.0f, 1.0f, &arg3->ox1, &arg3->oy1, &arg3->oz1);
    mtxf_transform_point(M2C_ERROR(/* Read from unset register $f12 */), M2C_ERROR(/* Read from unset register $f14 */), 0.0f, 0.0f, &arg3->ox3, &arg3->oy3, &arg3->oz3);
    mtxf_transform_point(M2C_ERROR(/* Read from unset register $f12 */), M2C_ERROR(/* Read from unset register $f14 */), 1.0f, 0.0f, &arg3->ox2, &arg3->oy2, &arg3->oz2);
    if (arg3->approachTarget == NULL) {
        apply_plane_tilt_anim(arg0, arg2, arg3);
    }
    if ((arg3->playerIndex == -1) && (gCurrentPlayerIndex != -1)) {
        gCurrentRacerHandlingStat = 1.4f;
    }
    temp_f0_2 = arg2->x_velocity;
    temp_f2_2 = arg2->z_velocity;
    temp_f14 = arg2->y_velocity;
    temp_f2_3 = (f32) ((f64) sqrtf((temp_f0_2 * temp_f0_2) + (temp_f2_2 * temp_f2_2) + (temp_f14 * temp_f14)) - 2.0);
    var_f20 = temp_f2_3;
    if (arg3->vehicleID >= 5) {
        var_f20 = (f32) (((f64) temp_f2_3 - 2.0) * 0.5);
    }
    if (var_f20 < 0.0f) {
        var_f20 = 0.0f;
    }
    var_f0_4 = (f64) var_f20;
    if (var_f0_4 > 4.0) {
        var_f0_4 = (f64) 4.0f;
    }
    spA3 = 0;
    temp_v0_4 = arg3->trickType;
    var_f20_2 = (f32) (1.0 - (var_f0_4 * 0.25));
    temp_f2_4 = (f32) (((f64) gCurrentCourseHeight - 50.0) - (f64) arg2->trans.position.f[1]);
    if ((temp_v0_4 < 2) && (temp_v0_4 >= -1) && (temp_f2_4 < 0.0f)) {
        var_f20_2 = (f32) ((f64) var_f20_2 + ((f64) -temp_f2_4 / 25.0));
        if (gCurrentStickY < -0x14) {
            gCurrentStickY = -0x14;
        }
        if ((f64) var_f20_2 > 2.5) {
            var_f20_2 = 2.5f;
        }
        spA3 = 1;
    }
    temp_f2_5 = arg3->velocity;
    var_f14 = temp_f2_5;
    if (temp_f2_5 < 0.0f) {
        var_f14 = -var_f14;
    }
    var_f0_5 = temp_f2_5;
    if (temp_f2_5 < 0.0f) {
        var_f0_5 = -temp_f2_5;
    }
    if ((var_f0_5 + 4.0f) < var_f14) {
        var_f14 = var_f0_5 + 3.0f;
    }
    if (var_f14 > 12.0f) {
        var_f14 = 12.0f;
    }
    temp_f18 = (s32) var_f14;
    temp_f0_3 = var_f14 - (f32) temp_f18;
    temp_v1_2 = &gCurrentRacerMiscAssetPtr[temp_f18];
    spD4 = 0.01f;
    spD0 = 0.02f;
    spD8 = 0.004f;
    temp_f14_2 = (f32) (((f64) temp_v1_2->unk0 * (1.0 - (f64) temp_f0_3)) + (f64) (temp_v1_2->unk4 * temp_f0_3));
    if (arg3->groundedWheels != 0) {
        spD4 = 0.02f;
        spD0 = 0.01f;
        var_a1_2 = 0;
        var_t0 = 0;
        temp_f0_4 = (f64) var_f20_2;
        var_v1_3 = arg3;
        do {
            temp_v0_5 = var_v1_3->wheel_surfaces[0];
            var_t0 += 1;
            if ((temp_v0_5 != 0xFF) && (var_a1_2 < (s32) temp_v0_5)) {
                var_a1_2 = (s32) temp_v0_5;
            }
            var_v1_3 += 1;
        } while (var_t0 != 4);
        if (var_a1_2 == 4) {
            arg3->magnetTimer = 0;
        }
        if ((arg3->playerIndex == 0) && (var_a1_2 == 0xC) && (gCurrentButtonsPressed & 0x2000)) {
            gTajInteractStatus = 2;
        }
        if ((gCurrentRacerInput & 0x4000) && (gCurrentStickY >= -0x28) && ((f64) arg3->velocity >= -0.5)) {
            spD8 = 0.004f * 8.0f;
        }
        if ((arg3->boostTimer == 0) && (var_a1_2 == 3)) {
            sp48 = temp_f0_4;
            spDC = temp_f14_2;
            arg3->boostTimer = normalise_time(0x2D);
            arg3->boostType = 2;
            if (arg3->throttleReleased != 0) {
                arg3->boostType |= 4;
            }
            sp48 = temp_f0_4;
            spDC = temp_f14_2;
            racer_play_sound(arg2, 0x107);
            play_random_character_voice(arg2, 0x162, 8, 0x82);
            rumble_set(arg3->playerIndex, 8U);
        }
        if ((arg3->vehicleID >= 5) && ((f64) arg3->velocity > -6.0)) {
            spC8 = (f32) ((f64) spC8 * 0.6);
            spC4 = (f32) ((f64) spC4 * 0.3);
        }
        arg3->trickType = 0;
        if ((gCurrentRacerInput & 0x4000) && (gNumViewports < 3)) {
            arg2->particleEmittersEnabled = 3;
        }
        gCurrentStickY = (s32) ((f64) (f32) gCurrentStickY * (1.0 - temp_f0_4));
        if (gCurrentStickY > 0) {
            gCurrentStickY = 0;
        }
    }
    temp_v0_6 = arg3->vehicleID;
    var_t0_2 = 0;
    if (spA3 == 0) {
        var_t0_2 = (s32) (var_f20_2 * 4608.0f);
    }
    if (temp_v0_6 >= 6) {
        var_t0_2 = 0;
    }
    if (temp_v0_6 == 0xA) {
        var_f20_2 = 0.0f;
        var_t0_2 = 0;
    }
    spDC = temp_f14_2;
    apply_vehicle_rotation_offset(arg3, arg0, 0, (s16) var_t0_2, 0);
    var_f14_2 = temp_f14_2;
    if (arg3->unk1FE == 0) {
        arg2->particleEmittersEnabled |= 0x100;
        var_f20_2 = 5.5f;
    }
    if (arg3->unk1FE == 1) {
        var_f20_2 = 2.0f;
    }
    if ((f64) arg3->buoyancy != 0.0) {
        gCurrentStickY = -0x3C;
        var_f2_2 = arg3->buoyancy - 20.0f;
        if ((f64) var_f2_2 < 0.0) {
            var_f2_2 = 0.0f;
        }
        var_f20_2 = -1.0f - (var_f2_2 / 10.0f);
        if ((f64) var_f20_2 < -4.0) {
            var_f20_2 = -4.0f;
        }
    }
    if (gRaceStartTimer != 0) {
        var_f20_2 = 1.0f;
    }
    if (arg3->vehicleIDPrev == 0xC) {
        if (arg2->animationID < 3) {
            var_f20_2 = 4.0f;
        } else {
            var_f20_2 = 0.0f;
        }
    }
    var_f20_3 = var_f20_2 * gCurrentRacerWeightStat;
    arg2->y_velocity -= var_f20_3;
    if ((arg3->zipperDirCorrection != 0) && (arg3->spinout_timer == 0)) {
        temp_v1_3 = arg3->steerVisualRotation;
        arg3->magnetTimer = 0;
        arg3->spinout_timer = 0;
        arg3->trickType = 0;
        var_v0_3 = arg3->zipperObj->trans.rotation.s[0] - (temp_v1_3 & 0xFFFF);
        if (var_v0_3 >= 0x8001) {
            var_v0_3 += 0xFFFF0001;
        }
        if (var_v0_3 < -0x8000) {
            var_v0_3 += 0xFFFF;
        }
        arg3->steerVisualRotation = temp_v1_3 + ((s32) (var_v0_3 * arg0) >> 3);
        if (((var_v0_3 < 0x400) && (var_v0_3 >= -0x3FF)) || (arg3->playerIndex == -1)) {
            if (arg3->playerIndex != -1) {
                spDC = var_f14_2;
                sound_play_spatial(0x107U, arg2->trans.position.f[0], arg2->trans.position.f[1], arg2->trans.position.f[2], NULL);
                play_random_character_voice(arg2, 0x162, 8, 0x82);
            }
            spDC = var_f14_2;
            arg3->boostTimer = normalise_time(0x2D);
            arg3->boostType = 2;
            if (arg3->throttleReleased != 0) {
                arg3->boostType |= 4;
            }
            spDC = var_f14_2;
            rumble_set(arg3->playerIndex, 8U);
            arg3->zipperDirCorrection = 0;
        } else {
            arg2->x_velocity = (f32) ((f64) arg2->x_velocity * 0.75);
            arg2->y_velocity = (f32) ((f64) arg2->y_velocity * 0.75);
            arg2->z_velocity = (f32) ((f64) arg2->z_velocity * 0.75);
        }
    }
    if (arg3->spinout_timer != 0) {
        temp_a0 = arg3->x_rotation_offset;
        if (arg3->unk1F1 == 0) {
            arg3->unk1F1 = 1;
        }
        if ((arg3->groundedWheels != 0) || (arg3->unk1F1 == 2)) {
            arg3->unk1F1 = 2;
            temp_v1_4 = arg3->z_rotation_offset;
            temp_t7 = arg0 << 0xB;
            arg3->x_rotation_offset -= temp_t7;
            if ((temp_t7 + temp_v1_4) > 0) {
                var_t4_2 = temp_v1_4 + temp_t7;
                if (temp_v1_4 <= 0) {
                    arg3->z_rotation_offset = 0;
                } else {
                    goto block_181;
                }
            } else {
                var_t4_2 = temp_v1_4 + temp_t7;
block_181:
                arg3->z_rotation_offset = var_t4_2;
            }
            if (((f64) arg3->velocity > -2.0) && (arg3->groundedWheels >= 3)) {
                arg3->spinout_timer = 0;
            }
        } else {
            arg3->z_rotation_offset += arg0 << 0xB;
        }
        if ((arg3->groundedWheels != 0) && (((var_at = temp_a0 < -0x5FFF, ((temp_a0 < 0x6001) == 0)) && (var_at = temp_a0 < -0x5FFF, ((arg3->x_rotation_offset < 0x6001) != 0))) || ((var_at == 0) && (arg3->x_rotation_offset < -0x5FFF)) || ((temp_a0 > 0) && (arg3->x_rotation_offset <= 0)))) {
            spDC = var_f14_2;
            racer_play_sound(arg2, 0xC);
            if (arg3->playerIndex != -1) {
                gCameraObject->shakeMagnitude = 6.0f;
            }
        }
        gCurrentRacerInput &= 0xFFFF5FFF;
        arg3->spinout_timer -= arg0;
        arg3->boostTimer = 0;
        arg3->brake = 1.0f;
        if (arg3->spinout_timer <= 0) {
            arg3->spinout_timer = 0;
            arg3->unk1F1 = 0;
        }
        temp_v1_5 = arg2->trans.rotation.s[1];
        var_v0_4 = 0xD800 - (temp_v1_5 & 0xFFFF);
        if (var_v0_4 >= 0x8001) {
            var_v0_4 += 0xFFFF0001;
        }
        if (var_v0_4 < -0x8000) {
            var_v0_4 += 0xFFFF;
        }
        arg2->trans.rotation.s[1] = temp_v1_5 + ((s32) (var_v0_4 * arg0) >> 4);
    } else {
        temp_v0_7 = arg3->trickType;
        if ((temp_v0_7 == 1) || (temp_v0_7 == -1)) {
            temp_v1_6 = arg3->x_rotation_vel;
            arg3->x_rotation_vel = temp_v1_6 + (temp_v0_7 * 0x600 * arg0);
            spC8 = 1.2f;
            if (temp_v0_7 == 1) {
                if (temp_v1_6 > 0) {
                    arg3->unk1D4 = 1;
                }
                if ((temp_v1_6 < 0) && (arg3->x_rotation_vel >= 0) && (arg3->unk1D4 != 0)) {
                    arg3->trickType = 0;
                    arg3->x_rotation_vel = 0;
                }
            } else {
                if (temp_v1_6 < 0) {
                    arg3->unk1D4 = 1;
                }
                if ((temp_v1_6 > 0) && (arg3->x_rotation_vel <= 0) && (arg3->unk1D4 != 0)) {
                    arg3->trickType = 0;
                    arg3->x_rotation_vel = 0;
                }
            }
        } else if ((temp_v0_7 == 2) || (temp_v0_7 == -2)) {
            temp_v1_7 = arg2->trans.rotation.s[1];
            if (arg3->unk1D5 == 0) {
                arg2->trans.rotation.s[1] = temp_v1_7 + (temp_v0_7 * 0x180 * arg0);
            }
            if (!(gCurrentRacerInput & 0x10)) {
                arg3->unk1D5 = 0;
            }
            temp_v0_8 = arg3->unk1D5;
            if (temp_v0_8 > 0) {
                arg3->unk1D5 = temp_v0_8 - arg0;
            } else {
                arg3->unk1D5 = 0;
            }
            temp_v1_8 = arg3->x_rotation_vel;
            arg3->x_rotation_vel = temp_v1_8 - ((s32) (temp_v1_8 * arg0) >> 4);
            arg2->x_velocity = arg3->velocity * arg3->ox1;
            arg2->y_velocity = arg3->velocity * arg3->oy1;
            arg2->z_velocity = arg3->velocity * arg3->oz1;
            if (arg3->trickType == 2) {
                if (temp_v1_7 > 0) {
                    arg3->unk1D4 = 1;
                }
                var_at_2 = temp_v1_7 < 0x4001;
                if (temp_v1_7 < 0) {
                    var_at_2 = temp_v1_7 < 0x4001;
                    if (arg2->trans.rotation.s[1] >= 0) {
                        var_at_2 = temp_v1_7 < 0x4001;
                        if (arg3->unk1D4 != 0) {
                            arg3->trickType = 0;
                            arg2->trans.rotation.s[1] = 0;
                            spDC = var_f14_2;
                            spB8 = (s32) temp_v1_7;
                            arg3->boostTimer = normalise_time(0xA);
                            arg3->boostType = 0;
                            if (arg3->throttleReleased != 0) {
                                arg3->boostType |= 4;
                            }
                            var_at_2 = temp_v1_7 < 0x4001;
                        }
                    }
                }
                if ((var_at_2 == 0) && (arg2->trans.rotation.s[1] < -0x4000) && (gCurrentRacerInput & 0x10)) {
                    arg3->unk1D5 = 0x3C;
                }
            } else {
                if (temp_v1_7 < 0) {
                    arg3->unk1D4 = 1;
                }
                var_at_3 = temp_v1_7 < -0x4000;
                if (temp_v1_7 > 0) {
                    var_at_3 = temp_v1_7 < -0x4000;
                    if (arg2->trans.rotation.s[1] <= 0) {
                        var_at_3 = temp_v1_7 < -0x4000;
                        if (arg3->unk1D4 != 0) {
                            arg3->trickType = 0;
                            arg2->trans.rotation.s[1] = 0;
                            spDC = var_f14_2;
                            spB8 = (s32) temp_v1_7;
                            arg3->boostTimer = normalise_time(0xA);
                            arg3->boostType = 0;
                            if (arg3->throttleReleased != 0) {
                                arg3->boostType |= 4;
                            }
                            var_at_3 = temp_v1_7 < -0x4000;
                        }
                    }
                }
                if ((var_at_3 != 0) && (arg2->trans.rotation.s[1] >= 0x4001) && (gCurrentRacerInput & 0x10)) {
                    arg3->unk1D5 = 0x3C;
                }
            }
        } else {
            temp_a0_2 = arg3->steerAngle;
            spA1 = 0;
            if (arg3->groundedWheels != 0) {
                if (gCurrentRacerInput & 0x10) {
                    spA1 = 1;
                }
                gCurrentRacerInput &= ~0x10;
            }
            if (arg3->groundedWheels < 2) {
                temp_v1_9 = arg2->trans.rotation.s[1];
                var_a0_2 = 0;
                if (temp_v1_9 >= 0x3001) {
                    var_a0_2 = temp_v1_9 - 0x3000;
                    if (var_a0_2 >= 0x1001) {
                        var_a0_2 = 0x1000;
                    }
                } else if (temp_v1_9 < -0x3000) {
                    temp_a0_3 = temp_v1_9 + 0x3000;
                    var_a0_2 = -temp_a0_3;
                    if (temp_a0_3 < -0x1000) {
                        var_a0_2 = --0x1000;
                    }
                }
                var_t0_3 = (s32) ((f32) temp_a0_2 * (f32) (1.0 - (f64) ((f32) var_a0_2 / 4096.0f)));
                if (gCurrentRacerInput & 0x10) {
                    arg2->particleEmittersEnabled |= 0xC0;
                    arg3->x_rotation_vel -= (s32) (var_t0_3 * 0x10 * arg0) >> 1;
                }
                arg3->x_rotation_vel -= (s32) (var_t0_3 * arg0 * 0x14) >> 1;
                temp_v1_10 = arg3->x_rotation_vel;
                arg3->x_rotation_vel = temp_v1_10 - ((s32) (temp_v1_10 * arg0) >> 4);
                if (arg3->zipperDirCorrection == 0) {
                    if ((gCurrentPlayerIndex != -1) && (arg3->raceFinished == 0)) {
                        temp_t5 = (s16) -arg3->x_rotation_vel >> 6;
                        var_t0_4 = temp_t5;
                        if ((gCurrentRacerInput & 0x10) && (gCurrentRacerInput & 0x4000)) {
                            var_t0_4 = temp_t5 * 2;
                        }
                        var_t0_3 = (s32) ((f32) var_t0_4 * gCurrentRacerHandlingStat);
                        arg3->steerVisualRotation -= var_t0_3 * arg0;
                    } else {
                        temp_t9 = gCurrentStickX * 4;
                        var_t0_3 = temp_t9;
                        arg3->steerVisualRotation -= temp_t9 * arg0;
                    }
                }
            } else {
                temp_v1_11 = arg3->x_rotation_vel;
                var_v0_5 = -(temp_v1_11 & 0xFFFF);
                var_t0_3 = temp_a0_2 * 4;
                if (var_v0_5 >= 0x8001) {
                    var_v0_5 += 0xFFFF0001;
                }
                if (var_v0_5 < -0x8000) {
                    var_v0_5 += 0xFFFF;
                }
                arg3->x_rotation_vel = temp_v1_11 + ((s32) (var_v0_5 * arg0) >> 4);
                if (gCurrentRacerInput & 0x10) {
                    var_t0_3 = temp_a0_2 * 6;
                }
                arg3->steerVisualRotation -= var_t0_3 * arg0;
            }
            temp_t6 = gCurrentRacerInput & 0x10;
            var_v0_6 = temp_t6;
            if ((temp_t6 == 0) || (arg3->groundedWheels == 0) || (arg3->zipperDirCorrection != 0)) {
                var_f20_3 = (f32) ((f64) (arg3->velocity * (f32) var_t0_3) * 0.00015000000673321665);
                arg2->x_velocity -= arg3->ox3 * var_f20_3;
                arg2->y_velocity -= arg3->oy3 * var_f20_3;
                arg2->z_velocity -= arg3->oz3 * var_f20_3;
                var_v0_6 = gCurrentRacerInput & 0x10;
            }
            var_t0_5 = gCurrentStickY;
            if ((gCurrentPlayerIndex != -1) && (arg3->raceFinished == 0)) {
                var_t0_5 = (s32) arg3->unk1E8;
            }
            var_f0_6 = (f64) -arg3->velocity;
            if (var_f0_6 < 4.0) {
                var_f0_6 = (f64) 4.0f;
            }
            if (var_f0_6 > 14.0) {
                var_f0_6 = (f64) 14.0f;
            }
            temp_f4 = (s32) ((f32) var_t0_5 * (f32) (var_f0_6 / 7.0));
            if (var_v0_6 == 0) {
                temp_v1_12 = arg2->trans.rotation.s[1];
                arg2->trans.rotation.s[1] = temp_v1_12 - ((s32) (temp_v1_12 * arg0) >> 4);
                arg2->trans.rotation.s[1] -= (s32) ((temp_f4 >> 1) * 0x13 * arg0) >> 1;
            } else {
                temp_v1_13 = arg2->trans.rotation.s[1];
                arg2->trans.rotation.s[1] = temp_v1_13 - ((s32) (temp_v1_13 * arg0) >> 4);
                arg2->trans.rotation.s[1] -= (s32) ((temp_f4 >> 1) * 0x1E * arg0) >> 1;
            }
            if (arg3->tappedR != 0) {
                arg3->tappedR = 0;
                if ((arg3->groundedWheels == 0) && ((f64) arg3->velocity < -6.5) && (arg3->waterTimer == 0)) {
                    if (gCurrentStickX >= 0x29) {
                        arg3->trickType = -1;
                    }
                    if (gCurrentStickX < -0x28) {
                        arg3->trickType = 1;
                    }
                    if (gCurrentStickY >= 0x29) {
                        arg3->trickType = -2;
                    } else if (arg3->trickType == 0) {
                        arg3->trickType = 2;
                    }
                    arg3->unk1D4 = 0;
                    arg3->unk1D5 = 0;
                }
            }
        }
    }
    if (gCurrentPlayerIndex != -1) {
        if (arg3->velocity < -4.0f) {
            temp_v0_9 = arg2->particleEmittersEnabled;
            if ((temp_v0_9 & 0xC0) != 0xC0) {
                arg2->particleEmittersEnabled = temp_v0_9 | 0xC;
            }
        }
    }
    spDC = var_f14_2;
    temp_v0_10 = arg3->boostTimer;
    var_f14_3 = (f32) ((f64) (var_f14_2 * handle_racer_top_speed(arg2, arg3)) * 1.8);
    if (temp_v0_10 > 0) {
        if (gRaceStartTimer == 0) {
            arg3->throttle = 1.0f;
            var_f14_3 = 2.0f;
            arg3->boostTimer = temp_v0_10 - arg0;
            arg2->particleEmittersEnabled |= 0xC0;
        }
    } else {
        arg3->boostTimer = 0;
    }
    if ((arg3->zipperDirCorrection == 0) && (gRaceStartTimer == 0)) {
        if ((arg3->groundedWheels == 0) && ((f64) spC8 < 0.4) && (arg3->vehicleID != 0xA)) {
            spC8 = 0.4f;
        }
        temp_f0_5 = spC8 * var_f14_3;
        arg2->x_velocity -= arg3->ox1 * temp_f0_5;
        arg2->y_velocity -= arg3->oy1 * temp_f0_5;
        arg2->z_velocity -= arg3->oz1 * temp_f0_5;
        temp_v1_14 = arg3->groundedWheels;
        if ((temp_v1_14 >= 3) || ((f64) arg3->velocity < 1.0) || (arg3->vehicleID == 0xA)) {
            if (temp_v1_14 == 0) {
                spC4 /= 2.0f;
            }
            temp_f0_6 = spC4 * (var_f14_3 / 2.0f);
            arg2->x_velocity += arg3->ox1 * temp_f0_6;
            arg2->y_velocity += arg3->oy1 * temp_f0_6;
            arg2->z_velocity += arg3->oz1 * temp_f0_6;
        }
        var_f12 = arg3->velocity * arg3->velocity;
        if (arg3->velocity < 0.0f) {
            var_f12 = -var_f12;
        }
        if ((var_f12 < 1.0f) && !(gCurrentRacerInput & 0x8000)) {
            var_f20_4 = arg3->velocity * spD8 * 8.0f;
        } else {
            var_f20_4 = var_f12 * spD8;
        }
        arg2->x_velocity -= arg3->ox1 * var_f20_4;
        arg2->y_velocity -= arg3->oy1 * var_f20_4;
        arg2->z_velocity -= arg3->oz1 * var_f20_4;
        temp_f0_7 = arg3->lateral_velocity;
        var_f20_5 = temp_f0_7 * temp_f0_7 * spD4;
        if (temp_f0_7 < 0.0f) {
            var_f20_5 = -var_f20_5;
        }
        temp_f20 = var_f20_5 + (temp_f0_7 * spD4 * 4.0f);
        arg2->x_velocity -= arg3->ox3 * temp_f20;
        arg2->y_velocity -= arg3->oy3 * temp_f20;
        arg2->z_velocity -= arg3->oz3 * temp_f20;
        temp_v0_11 = arg3->trickType;
        if ((temp_v0_11 == 1) || (temp_v0_11 == -1)) {
            temp_f12 = (f32) ((f64) arg3->velocity * 0.058823529411764705 * 1.5);
            spEC = temp_f12;
            temp_v1_15 = arg3->x_rotation_vel;
            var_f20_6 = coss_f(arg3->x_rotation_vel) * temp_f12 * (f32) arg3->trickType;
            if ((temp_v1_15 >= 0x4001) || (temp_v1_15 < -0x4000)) {
                var_f20_6 *= 2.0f;
            }
            arg2->x_velocity -= arg3->ox3 * var_f20_6;
            arg2->y_velocity -= arg3->oy3 * var_f20_6;
            arg2->z_velocity -= arg3->oz3 * var_f20_6;
            spEC = temp_f12;
            var_f12 = temp_f12;
            temp_f20_2 = (f32) ((f64) (sins_f(arg3->x_rotation_vel) * var_f12 * (f32) arg3->trickType) * 1.5);
            arg2->x_velocity -= arg3->ox2 * temp_f20_2;
            arg2->y_velocity -= arg3->oy2 * temp_f20_2;
            arg2->z_velocity -= arg3->oz2 * temp_f20_2;
        }
        temp_f2_6 = arg3->unk34;
        var_f20_7 = temp_f2_6 * temp_f2_6 * spD0;
        if (temp_f2_6 < 0.0f) {
            var_f20_7 = -var_f20_7;
        }
        var_f20_3 = var_f20_7 + (temp_f2_6 * spD0 * 4.0f);
        arg2->x_velocity -= arg3->ox2 * var_f20_3;
        arg2->y_velocity -= arg3->oy2 * var_f20_3;
        arg2->z_velocity -= arg3->oz2 * var_f20_3;
        temp_f0_8 = (f64) arg3->forwardVel;
        arg3->forwardVel = (f32) (temp_f0_8 - ((temp_f0_8 + ((f64) arg3->velocity * *(&D_800E6538 + 4))) * 0.125));
        spEC = var_f12;
    }
    arg3->unk10C = 0;
    temp_v0_12 = arg3->y_rotation_vel;
    arg3->y_rotation_vel = temp_v0_12 + ((s32) (gCurrentCarSteerVel - temp_v0_12) >> 3);
    arg2->trans.rotation.s[0] = arg3->steerVisualRotation + arg3->y_rotation_vel;
    temp_v1_16 = arg3->z_rotation_vel;
    arg3->z_rotation_vel = temp_v1_16 + ((s32) (D_8011D558 - temp_v1_16) >> 3);
    arg2->trans.rotation.s[2] = arg3->x_rotation_vel + arg3->z_rotation_vel;
    if (arg3->magnetTimer != 0) {
        arg2->x_velocity = gRacerMagnetVelX;
        arg2->z_velocity = gRacerMagnetVelZ;
    }
    if (arg3->approachTarget == NULL) {
        var_f20_8 = arg2->x_velocity;
        var_f12_2 = arg2->z_velocity;
        if (arg3->unk1D2 != 0) {
            var_f20_8 = (f32) ((f64) var_f20_8 + ((f64) arg3->unk11C * 0.5));
            var_f12_2 = (f32) ((f64) var_f12_2 + ((f64) arg3->unk120 * 0.5));
        }
        if (gRacerInputBlocked != 0) {
            temp_f0_9 = (f64) var_f20_8;
            if ((temp_f0_9 > 0.5) || (temp_f0_9 < -0.5)) {
                var_f20_3 = (f32) (temp_f0_9 * 0.65);
            } else {
                var_f20_3 = 0.0f;
            }
            temp_f0_10 = (f64) var_f12_2;
            if ((temp_f0_10 > 0.5) || (temp_f0_10 < -0.5)) {
                var_f12_3 = (f32) (temp_f0_10 * 0.65);
            } else {
                var_f12_3 = 0.0f;
            }
        } else {
            var_f20_3 = var_f20_8 + arg3->unk84;
            var_f12_3 = var_f12_2 + arg3->unk88;
        }
        spEC = var_f12_3;
        var_f12_4 = var_f12_3;
        if ((move_object(arg2, var_f20_3 * arg1, arg2->y_velocity * arg1, var_f12_3 * arg1) != 0) && (gCurrentPlayerIndex != -1)) {
            sp5F = 1;
        }
    } else {
        racer_approach_object(arg2, arg3, arg1);
        var_f12_4 = spEC;
    }
    temp_t0 = arg3->groundedWheels;
    if (gCurrentPlayerIndex == -1) {
        if ((arg3->vehicleIDPrev != 0xD) || (gRaceStartTimer != 0)) {
            spB8 = (s32) temp_t0;
            spEC = var_f12_4;
            onscreen_ai_racer_physics(arg2, arg3, arg0);
        } else {
            arg3->groundedWheels = 0;
            arg3->unk1E3 = 0;
        }
    } else {
        spB8 = (s32) temp_t0;
        spEC = var_f12_4;
        func_80054FD0(arg2, arg3, arg0);
    }
    if ((temp_t0 == 0) && (arg3->groundedWheels != 0) && (arg3->spinout_timer != 0)) {
        spEC = var_f12_4;
        racer_play_sound(arg2, 0xC);
        if (arg3->playerIndex != -1) {
            gCameraObject->shakeMagnitude = 6.0f;
        }
    }
    temp_v0_13 = arg3->unk1D2;
    if (temp_v0_13 != 0) {
        arg3->unk1D2 = temp_v0_13 - arg0;
        if (arg3->unk1D2 < 0) {
            arg3->unk1D2 = 0;
        }
    } else {
        temp_f0_11 = 1.0f / arg1;
        var_f20_3 = ((arg2->trans.position.f[0] - spE8) - D_8011D548) * temp_f0_11;
        arg2->y_velocity = (arg2->trans.position.f[1] - spE4) * temp_f0_11;
        var_f12_4 = ((arg2->trans.position.f[2] - spE0) - D_8011D54C) * temp_f0_11;
    }
    if (gRaceStartTimer == 0x64) {
        arg2->y_velocity = -5.0f;
    }
    arg2->x_velocity = var_f20_3;
    arg2->z_velocity = var_f12_4;
    gCurrentRacerTransform.rotation.s[0] = -arg2->trans.rotation.s[0];
    gCurrentRacerTransform.rotation.s[1] = -arg2->trans.rotation.s[1];
    gCurrentRacerTransform.rotation.s[2] = 0;
    gCurrentRacerTransform.position.f[0] = 0.0f;
    gCurrentRacerTransform.position.f[1] = 0.0f;
    gCurrentRacerTransform.position.f[2] = 0.0f;
    gCurrentRacerTransform.scale = 1.0f;
    mtxf_from_inverse_transform((f32 (*)[4][4]) &sp60[0][0], &gCurrentRacerTransform);
    mtxf_transform_point(M2C_ERROR(/* Read from unset register $f12 */), M2C_ERROR(/* Read from unset register $f14 */), arg2->y_velocity, arg2->z_velocity, &arg3->lateral_velocity, &arg3->unk34, &arg3->velocity);
    temp_v1_17 = arg2->attachPoints;
    if ((temp_v1_17 != NULL) && (temp_v1_17->count >= 3)) {
        temp_v0_14 = temp_v1_17->obj[2];
        temp_v0_14->modelIndex += 1;
        temp_v0_14->trans.rotation.s[0] = 0x4000;
        if (temp_v0_14->header->numberOfModelIds == temp_v0_14->modelIndex) {
            temp_v0_14->modelIndex = 0;
        }
    }
    temp_v1_18 = arg2->attachPoints;
    if ((temp_v1_18 != NULL) && (temp_v1_18->count >= 3)) {
        if ((arg3->groundedWheels != 0) || (spA2 != 0)) {
            temp_v0_15 = temp_v1_18->obj[0];
            temp_f0_12 = temp_v0_15->trans.position.f[1];
            if (temp_f0_12 > 0.0f) {
                temp_v0_15->trans.position.f[1] = (f32) ((f64) temp_f0_12 - 2.0);
            } else {
                temp_v0_15->trans.position.f[1] = 0.0f;
            }
            temp_v0_15->trans.flags &= 0xBFFF;
            temp_v0_16 = arg2->attachPoints->obj[1];
            temp_f0_13 = temp_v0_16->trans.position.f[1];
            if (temp_f0_13 > 0.0f) {
                temp_v0_16->trans.position.f[1] = (f32) ((f64) temp_f0_13 - 2.0);
            } else {
                temp_v0_16->trans.position.f[1] = 0.0f;
            }
            temp_v0_16->trans.flags &= ~0x4000;
        } else {
            temp_v0_17 = temp_v1_18->obj[0];
            temp_f0_14 = temp_v0_17->trans.position.f[1];
            if (temp_f0_14 < 20.0f) {
                temp_v0_17->trans.position.f[1] = temp_f0_14 + 1.0f;
            } else {
                temp_v0_17->trans.flags |= 0x4000;
            }
            temp_v0_18 = arg2->attachPoints->obj[1];
            temp_f0_15 = temp_v0_18->trans.position.f[1];
            if (temp_f0_15 < 20.0f) {
                temp_v0_18->trans.position.f[1] = temp_f0_15 + 1.0f;
            } else {
                temp_v0_18->trans.flags |= 0x4000;
            }
        }
    }
    if ((gCurrentPlayerIndex != -1) && (arg3->boostTimer == 0) && (gNumViewports < 2)) {
        temp_t0_2 = ((s32) (arg3->boostType & 4) >> 2) + 9;
        temp_v1_19 = (arg3->racerIndex << 7) + get_misc_asset(0x14);
        if (temp_t0_2 >= 0xA) {
            if (((s32) temp_v1_19->unk70 > 0) || ((f64) temp_v1_19->unk74 > 0.0)) {
                arg2->particleEmittersEnabled |= 1 << temp_t0_2;
            }
        } else {
            temp_v0_19 = temp_v1_19->unk70;
            var_at_4 = (s32) temp_v0_19 < 2;
            if ((temp_v0_19 == 2) && (var_at_4 = (s32) temp_v0_19 < 2, ((f64) temp_v1_19->unk74 < 0.5))) {
                arg2->particleEmittersEnabled |= 1 << temp_t0_2;
            } else if ((var_at_4 != 0) && (temp_v1_19->unk74 > 0.0f)) {
                arg2->particleEmittersEnabled |= 1 << temp_t0_2;
            }
        }
    }
    if (gCurrentPlayerIndex == -1) {
        arg2->particleEmittersEnabled = 0;
    }
    if (arg3->unk201 == 0) {
        arg2->particleEmittersEnabled = 0;
    }
    if (arg3->vehicleIDPrev < 5) {
        update_vehicle_particles(arg2, arg0);
    }
    if (spA1 != 0) {
        gCurrentRacerInput |= 0x10;
    }
    second_racer_camera_update(arg2, arg3, 1, arg1);
    if (sp5F != 0) {
        func_800230D0(arg2, arg3);
    }
}
